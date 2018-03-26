import time
import json
import requests
import sys

from time import sleep, clock
from vkscript import CODE_GROUP, CODE_FRIENDS

# from vkapi import TOKEN



TOKEN = 'a2bad147ba553f5fb6dfbfc048f86452ed9ec02d7bb3b9348593c38e5c8328ce4dbd5b1106083b963c1f8'
# TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

# Для метода execute:
token = TOKEN
url = "https://api.vk.com/method/execute?"
api_v = 5.73
APP = 6413027  # application ID


# Функция отображает процесс обработки шага программы (прогресс бар):
def output_result(*args):
    for x in range(0, len(*args)+1):
        sys.stdout.write('\r')
        part = float(x) / (len(*args))
        symbols_num = int(30 * part)
        sys.stdout.write("%-30s  %d%%  " % ('|' * symbols_num, part * 100))
        sys.stdout.flush()
        time.sleep(0.008)


# 1. Функция получает id пользователя и возвращает его значение
def get_user_id(link):
    user_id = link
    if 'vk.com/' in link:  # проверяем эту ссылку
        user_id = link.split('/')[-1]  # если да, то получаем его последнюю часть
    if not user_id.replace('id', '').isdigit():  # если в нем после отсечения 'id' сами цифры - это и есть id
        params = {
            'screen_name': user_id,
            'v': api_v
        }
        response = requests.get('https://api.vk.com/method/utils.resolveScreenName', params)
        user_id = response.json()['response']['object_id']
    else:
        user_id = user_id.replace('id', '')
    return int(user_id)


# 2. Функция поиска друзей методом friend.get.
# Возвращает список идентификаторов друзей пользователя и расширенную информацию по параметру fields.
def get_friends(user_id):
    CODE = CODE_FRIENDS % (user_id)

    data = dict(code=CODE, access_token=token, v=api_v)
    execute = requests.post(url=url, data=data, timeout=10)
    response_data = execute.json()
    time.sleep(1)
    friends = response_data['response'][0]

    # Найдем списки друзей в активном статусе ('status') и удаленных или забаненных ('deactivated'):
    friends_status = [friend for friend in friends['items'] if ('status') in friend]
    friends_deactiv = [friend for friend in friends['items'] if friend.get('deactivated')]
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
    time.sleep(1)
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


# 5. Функция возвращает список групп для каждого друга пользователя. Метод groups.get
def get_groups_friends(user_id):
    friends_id = get_friends(user_id)
    groups_friends = []

    for friend in friends_id:
        CODE = CODE_GROUP % (friend, 0)

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        time.sleep(1)
        groups_friends.append(response_data['response'][0]['items'])

        output_result(groups_friends)

    groups_id_friends = [groups for friend in groups_friends for groups in friend]
    # output_result(groups_id_friends)


    return set(groups_id_friends)


# link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя
# user_id = '5030613'
user_id = '171691064'


def main():
    start_time = time.clock()
    # user_id = input('Введите id или ссылку на страницу пользователя (в конце не забудьте пробел): \n')
    # user_id = get_user_id(user_id)
    print(f'Идентификатор пользователя: id = {user_id}')


    friends_id = get_friends(user_id)
    print(f"Количество друзей пользователя: {len(friends_id)}")


    groups_user = get_groups_user(user_id)
    groups_user_id = get_groups_user_id(user_id)
    print(f"Количество групп пользователя: {len(get_groups_user_id(user_id))}")


    print('Идет процесс обработки поиска групп друзей...')
    groups_friends = get_groups_friends(user_id)
    # output_result(groups_friends)
    print('\nПоиск завершен')
    print(f'Количество групп друзей пользователя: {len(groups_friends)}')


    # Определим группы, в которых есть друзья пользователя.
    # Найдем пересечение множеств двух списков и получим множество общих с друзьями групп.
    groups_with_friends = set(groups_user_id) & set(groups_friends)
    print(f'Количество групп, в которых есть друзья: {len(groups_with_friends)}')


    # Найдем список групп, в которых нет друзей пользователя.
    # Условие для поиска: для group в списке groups_user,
    # если group нет в groups_friends или groups_friends.add() возвращает None, то добавить group в новый список.
    print('Идет процесс обработки поиска групп пользователя, в которых нет друзей ...')
    groups_without_friends = [group for group in groups_user_id \
                              if not (group in groups_friends or groups_friends.add(group))]
    # Прогресс бар:
    output_result(groups_without_friends)
    print('\nПоиск завершен')
    print(f"Количество групп (без друзей): {len(groups_without_friends)}")


    # Создадим новый список, в который добавим группы без друзей для вывода на запись в файл.
    print('Идет обработка полученных групп...')
    groups_result = []
    for group in groups_user:
        if group['id'] in groups_without_friends:
            groups_result.append({
                'name': group.get('name'),
                'gid': group.get('id'),
                'members_count': group.get('members_count')
            })

    output_result(groups_result)

    # Запишем полученные группы в файл.
    print('Идет запись полученных групп в файл...')
    with open('groups_.json', 'w', encoding='utf-8') as fw:
        data = groups_result
        json.dump(data, fw, sort_keys=True, indent=2, ensure_ascii=False)
        print('Запись в файл завершена')

    end_time = time.clock()

    print(f'Время выполнения программы {int(end_time - start_time)} seconds')


main()

