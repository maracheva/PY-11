import json
import requests
import sys

from time import sleep, clock
from vkscript import CODE_GROUP, CODE_FRIENDS, CODE_ISMEMBER

# from vkapi import TOKEN


TOKEN = 'cd549f8ad69255caa1c37c00a3afbc541d8bc21a8ff70ad656a3441c7d4f13f9c0eca306542f4217fa6a7'
# TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

# Все необходимые методы поиска будем выполнять с помощью метода execute.
# Данные для метода execute:
token = TOKEN
url = "https://api.vk.com/method/execute?"
api_v = 5.73

start_time = clock()

# Функция отображает процесс обработки шага программы:
def output_result(*args):
    for x in range(0, len(*args) + 1):
        sys.stdout.write('\r')
        part = float(x) / (len(*args))
        symbols_num = int(30 * part)
        sys.stdout.write("[%-30s]  %d%%  " % ('|' * symbols_num, part * 100))
        sys.stdout.flush()
        sleep(0.008)


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
def get_is_members(user_id):
    friends_id = get_friends(user_id)
    group_id_list = get_groups_user_id(user_id)

    all_members = []
    for group_id in group_id_list:
        CODE = CODE_ISMEMBER % (group_id, friends_id)

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        sleep(1)
        members = response_data['response']
        # output_result(members)
        if not any(element['member'] for element in members):
            all_members.append(group_id)
    # output_result(all_members)
    return all_members


# 6. Выведем результат.
def get_groups_result(user_id):
    groups_user_all = get_groups_user(user_id)  # расширенный список групп пользователя
    groups_without_friends = get_is_members(user_id)  # список групп без друзей
    groups_result = []

    for group in groups_user_all:
        if group['id'] in groups_without_friends:
            groups_result.append({
                'name': group.get('name'),
                'gid': group.get('id'),
                'members_count': group.get('members_count'),
            })

    return groups_result


end_time = clock()


# link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя
# user_id = '5030613'
# user_id = '171691064'

def main():
    user_id = input('Введите id или ссылку на страницу пользователя (в конце не забудьте пробел): \n')
    user_id = get_user_id(user_id)
    print(f'Идентификатор пользователя: id = {user_id}')

    friends_id = get_friends(user_id)
    print(f'Количество друзей пользователя: {len(friends_id)}')

    groups_user = get_groups_user(user_id)
    print(f'Количество групп пользователя: {len(groups_user)}')

    print('Идет процесс обработки групп пользователя...')

    groups_result = get_groups_result(user_id)
    print(f'Количество групп пользователя (без друзей): {len(groups_result)}')
    print('Процесс завершен')
    print('Идет процесс записи результата в файл...')
    groups_list = get_groups_result(user_id)
    with open('groups.json', 'w', encoding='utf-8') as fw:
        data = groups_list
        json.dump(data, fw, sort_keys=True, indent=2, ensure_ascii=False)
        print('Запись в файл завершена')

    print(f'Время выполнения программы {float(end_time - start_time)/60} ')


main()

'''
1. В качестве входных данных будет выступать ссылка на профиль пользователя. 
Нам понадобится цифровой id, который не всегда в ней указан,  
Поэтому с помощью метода utils.resolveScreenName мы получаем что нам нужно.
2. Функция get_friends(*args) находит всех друзей пользователя по методу friend.get.
Снчачла получили словарь friends типа {'count': int, 'items': [{}, {},...,{}]},
где значение по ключу 'items' будет представлять из себя список словарей.
Каждый словарь - данные по каждому другу пользователя, т.е:
'items': [
        {'id': '', 'first_name': '', 'last_name': '', 'status': '', 'online': 0},
        {'id': '', 'first_name': '', 'last_name': '', 'deactivated': '', 'online': 0}
        .....
        ]
По ключам 'deactivated' и 'status' получим списки удаленных/забанненых друзей и друзей в активном статусе.
Т.е. получим разделенные по статусу списки типа:
friends_status = [{'id': '', 'first_name': '', 'last_name': '', 'status': '', 'online': 0}, {},..., {}]
friends_deactiv = [{'id': '', 'first_name': '', 'last_name': '', 'deactivated': '', 'online': 0},..., {}]

Далее получим список только с id друзей пользователя friends_id_list из списка friends_status.
Таким образом, заранее исключили друзей со статусом 'deactivated',
и дальше не возникнит проблемы с удаленными друзьями.
3. Получим расширенную информацию по группам пользователя.
4. Получим список только с id групп пользователя.
5. Для поиска групп, где нет друзей, применим метод groups.isMember. 
Получили список словарей по всем друзьям для каждого id группы:
[{'member': 0, 'user_id': 8822}, {'member': 0, 'user_id': 20338},...].
Сделаем выборку по условию 'member' = 1. Если в списке нет 'member' = 1, добавим группу в новый список.
Так получим список групп group_id, в которых нет друзей.
Значение element['member'] = True, если оно не равно 0.
6. Оформим результат. 

'''
