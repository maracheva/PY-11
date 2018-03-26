import json
import requests
import sys
import time

from time import sleep, clock
from vkscript import CODE_GROUP, CODE_FRIENDS, CODE_getMEMBERS

# from vkapi import TOKEN


# TOKEN = 'cd549f8ad69255caa1c37c00a3afbc541d8bc21a8ff70ad656a3441c7d4f13f9c0eca306542f4217fa6a7'
TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

# Все необходимые методы поиска будем выполнять с помощью метода execute.
# Данные для метода execute:
token = TOKEN
url = "https://api.vk.com/method/execute?"
api_v = 5.73

# start_time = clock()
user_id = '171691064'

# Функция отображает процесс обработки шага программы:
def output_result(*args):
    for x in range(1, len(*args)+1):
        sys.stdout.write('\r')
        part = float(x) / (len(*args))
        symbols_num = int(30 * part)
        sys.stdout.write("%-30s  %d%%  " % ('|' * symbols_num, part * 100))
        sys.stdout.flush()
        time.sleep(0.008)


# 1. Функция получает id пользователя и возвращает его значение:
def get_user_id(link):
    id = link
    if 'vk.com/' in link:  # проверяем эту ссылку
        id = link.split('/')[-1]  # если да, то получаем его последнюю часть
    if not id.replace('id', '').isdigit():  # если в нем после отсечения 'id' сами цифры - это и есть id
        params = {
            'screen_name': id,
            'v': api_v
        }
        response = requests.get('https://api.vk.com/method/utils.resolveScreenName', params)
        id = response.json()['response']['object_id']
    else:
        id = id.replace('id', '')
    return int(id)


# 2. Функция поиска друзей методом friend.get.
# Возвращает список идентификаторов друзей пользователя и расширенную информацию по параметру fields.
def get_friends(user_id):
    CODE = CODE_FRIENDS % (user_id)

    data = dict(code=CODE, access_token=token, v=api_v)
    execute = requests.post(url=url, data=data, timeout=10)
    response_data = execute.json()
    sleep(1)
    friends = response_data['response'][0]
    # Найдем списки друзей в активном статусе ('status') и удаленных или забаненных ('deactivated'):
    friends_status = [friend for friend in friends['items'] if ('status') in friend]
    # Будем рассматривать только друзей с активным статусом.
    # Из списка друзей friends_status получим список только с id друзей пользователя:
    friends_id = [friend.get('id') for friend in friends_status]

    return friends_id


# 3. Функция находит  и возвращает список групп пользователя по id.
# Будем находить группы методом groups.get. Параметр extended=1 позволяет получить расширенную информацию о группе.
def get_groups_user(user_id):
    CODE = CODE_GROUP % (user_id, 1)

    data = dict(code=CODE, access_token=token, v=api_v)
    execute = requests.post(url=url, data=data, timeout=10)
    response_data = execute.json()
    sleep(1)
    # Получим словарь типа {'count': int, 'items': [{}, {}, ..., {}]}
    groups = response_data['response'][0]
    # Запишем в отдельный список полученные данные по группам.
    groups_list = groups.get('items')

    return groups_list


# 4. Функция возвращает список id групп:
def get_groups_user_id(user_id):
    groups_list = get_groups_user(user_id)
    groups_id_list = [element['id'] for element in groups_list]

    return groups_id_list


# 5. Опредлим, являются ли друзья пользователя членами сообществ пользователя
def get_members(user_id):
    group_id_list = get_groups_user_id(user_id)

    all_members = []
    for group_id in group_id_list:
        CODE = CODE_getMEMBERS % group_id

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        sleep(1)
        members = response_data['response']
        # Прогресс бар:
        # output_result(members)
        # print(f'Обработана группа {group_id}')

        if not any(element['count'] for element in members):
            all_members.append(group_id)

        output_result(all_members)
        print(f'Обработана группа {group_id}')

    # Прогресс бар:
    output_result(all_members)
    print('Список групп без друзей получен')

    return all_members


# link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя
user_id = '5030613'
# user_id = '171691064'

def main():
    start_time = clock()
    # user_id = input('Введите id или ссылку на страницу пользователя (в конце не забудьте пробел): \n')
    # user_id = get_user_id(user_id)
    print(f'Идентификатор пользователя: id = {user_id}')

    friends_id = get_friends(user_id)
    print(f'Количество друзей пользователя: {len(friends_id)}')

    groups_user = get_groups_user(user_id)
    print(f'Количество групп пользователя: {len(groups_user)}')

    # Создадим новый список, в который добавим группы без друзей, для вывода на запись в файл.
    print('Идет процесс обработки групп пользователя...')
    groups_without_friends = get_members(user_id)  # список групп без друзей
    groups_result = []
    for group in groups_user:
        if group['id'] in groups_without_friends:
            groups_result.append({
                'name': group.get('name'),
                'gid': group.get('id'),
                'members_count': group.get('members_count'),
            })
    # output_result(groups_result)
    print(f'\nКоличество групп пользователя (без друзей): {len(groups_result)}')
    print('Процесс завершен')

    print('Идет процесс записи результата в файл...')
    with open('groups.json', 'w', encoding='utf-8') as fw:
        data = groups_result
        json.dump(data, fw, sort_keys=True, indent=2, ensure_ascii=False)
        print('Запись в файл завершена')

    end_time = clock()
    print(f'Время выполнения программы {int(end_time - start_time)} sec')


main()

