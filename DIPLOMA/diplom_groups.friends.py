import time
import json
import requests
import sys

from time import sleep, clock
from vkscript import CODE_GROUP, CODE_FRIENDS

# from vkapi import TOKEN

start_time = time.clock()

TOKEN = 'b3d1ef8f5220b4dfde7f05bef16d67a4ad8ce090ce29b9d33de64a80c48330f5e187c610fafb70ff9f9e1'
# TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'

# Для метода execute:
token = TOKEN
url = "https://api.vk.com/method/execute?"
api_v = 5.73
APP = 6413027  # application ID


# Функция отображает процесс обработки шага программы:
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
    global friend
    friends_id = get_friends(user_id)
    groups_friends = []

    for friend in friends_id:
        CODE = CODE_GROUP % (friend, 0)

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        time.sleep(1)
        groups_friends.append(response_data['response'][0]['items'])

        # output_result(friends_id)

    groups_id_friends = [groups for friend in groups_friends for groups in friend]


    return set(groups_id_friends)


# 6. Получим список групп, общих с друзьями и без друзей.
def groups_user_and_friends(user_id):
    groups_user = get_groups_user_id(user_id)           # список id групп пользователя
    groups_friends = get_groups_friends(user_id)        # список групп друзей

    # Найдем пересечение множеств двух списков и получим множество общих с друзьями групп:
    groups_with_friends = set(groups_user) & set(groups_friends)

    # Найдем список групп, в которых нет друзей пользователя.
    # Условие для поиска: для group в списке groups_user,
    # если group нет в groups_friends или groups_friends.add() возвращает None, то добавить group в новый список.
    groups_without_friends = [group for group in groups_user \
                              if not (group in groups_friends or groups_friends.add(group))]


    return groups_without_friends



# 7. Выведем результат.
def get_groups_result(user_id):
    groups_user_all = get_groups_user(user_id)                  # расширенный список групп пользователя
    groups_without_friends = groups_user_and_friends(user_id)   # список групп без друзей
    groups_result = []

    for group in groups_user_all:
        if group['id'] in groups_without_friends:
            groups_result.append({
                    'name': group.get('name'),
                    'gid': group.get('id'),
                    'members_count': group.get('members_count')
            })

    return groups_result


end_time = time.clock()



# link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя
# user_id = '5030613'
# user_id = '171691064'
def main():
    user_id = input('Введите id или ссылку на страницу пользователя (в конце не забудьте пробел): \n')
    user_id = get_user_id(user_id)
    print(f'Идентификатор пользователя: id = {user_id}')

    friends_id = get_friends(user_id)
    print(f"Количество друзей пользователя: {len(friends_id)}")

    groups_user = get_groups_user(user_id)
    print(f"Количество групп пользователя: {len(groups_user)}")

    print('Идет процесс обработки поиска групп друзей...')
    groups_friends = get_groups_friends(user_id)
    # output_result(groups_friends)
    print('\nПоиск завершен')
    print(f'Количество групп друзей пользователя: {len(groups_friends)}')

    print('Идет процесс обработки поиска групп пользователя, в которых нет друзей ...')
    groups_without_friends = groups_user_and_friends(user_id)
    # output_result(groups_without_friends)
    print('\nПоиск завершен')
    print(f"Количество групп (без друзей): {len(groups_without_friends)}")

    print('Идет запись полученных групп в файл...')
    groups_list = get_groups_result(user_id)
    with open('groups_.json', 'w', encoding='utf-8') as fw:
        data = groups_list
        json.dump(data, fw, sort_keys=True, indent=2, ensure_ascii=False)
        print('Запись в файл завершена')

    print(f'Время выполнения программы {float(end_time - start_time)} seconds')

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
3.


'''