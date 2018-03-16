# coding: utf-8

import vk
import time
import json

TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
# TOKEN = '4810e7961c591569c8850e4dbe54581fc6edbbbf483d4a73458f0e820980994798216d27d5180fb6d100b'
# TOKEN = 'f06bf1792fa30f3f16841177882498b0e32e3fc57161de4b70eebfd35f4127ad243267fa721f3bb4c0e07'

api_v = 5.73
APP_ID = 6353308  # application ID
LOGIN_URL = 'perevoloki_85@mail.ru'
PASSWORD = 'samara'

# session = vk.AuthSession(app_id=APP_ID, user_login=LOGIN_URL, user_password=PASSWORD, scope='friends, groups')
session = vk.Session(access_token=TOKEN)
vkapi = vk.API(session, v=api_v, timeout=10, scope='friends, groups')

'''
В качестве входных данных будет выступать ссылка на профиль пользователя. 
Конкретно, нам понадобится цифровой id, который не всегда в ней указан, 
ведь многие используют возможность сделать ссылку на профиль на латинице. 
Поэтому с помощью метода utils.resolveScreenName мы получаем что нам нужно.
'''
link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя


# Функция получает id пользователя и возвращает его значение
def get_user_id(link):
    id = link
    if 'vk.com/' in link:  # проверяем эту ссылку
        id = link.split('/')[-1]  # если да, то получаем его последнюю часть
    if not id.replace('id', '').isdigit():  # если в нем после отсечения 'id' сами цифры - это и есть id
        id = vkapi.utils.resolveScreenName(screen_name=id)['object_id']  # если нет, получаем id с помощью метода API
    else:
        id = id.replace('id', '')
    return int(id)


# get_user_id(link)
user_id = get_user_id(link)


# Функция поиска друзей методом friend.get.
# Возвращает список идентификаторов друзей пользователя и расширенную информацию по параметру fields.
def get_friends(user_id):
    friends = vkapi.friends.get(user_id=user_id, fields='status')
    print(f"Количество друзей пользователя: {friends.get('count')}")
    '''
    Получили словарь типа {'count': int, 'items': [{}, {},...,{}]}, где значение по ключу 'items' будет 
    представлять из себя список словарей. 
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
    По этому списку и будем дальше находить группы друзей.
    Таким образом, заранее исключили друзей со статусом 'deactivated', и при поиске групп друзей 
    не возникнит проблемы с удаленными друзьями.
    '''
    friends_status = [friend for friend in friends['items'] if ('status') in friend]
    friends_deactiv = [friend for friend in friends['items'] if friend.get('deactivated')]
    print(f'Количество друзей в активном статусе: {len(friends_status)}')
    print(f'Количество друзей удаленных или забаненных: {len(friends_deactiv)}')

    # Из списка друзей friends_status получим список только с id друзей пользователя:
    friends_id_list = [friend.get('id') for friend in friends_status]
    # Запишем словарь типа {'id': [id1, id2, id3,...,idn]}
    friends_id_dict = {'id': friends_id_list}
    # print(friends_id_list)
    # print(friends_id_dict)

    return friends_id_list

friends_id = get_friends(user_id)

# Функция находит  и возвращает список групп пользователя по id.
# Будем находить группы методом groups.get. Параметр extended=1 позволяет получить расширенную информацию о группе.
def get_groups_user(*args):
    groups = vkapi.groups.get(user_id=user_id, extended=1)
    # Получили словарь типа {'count': int, 'items': [{}, {}, ..., {}]}
    print(f"Количество групп пользователя: {groups.get('count')}")
    # print('Список групп:')
    # for i, group in enumerate(groups['items']):
    #     print(f'{i+1}. {group}')

    # Получим словарь только с id групп пользователя:
    groups_id = vkapi.groups.get(user_id=user_id, extended=0)
    # Генератор списка id групп пользователя:
    groups_id_list = [id for id in groups_id['items']]
    print(groups_id_list)
    return groups_id_list


# get_groups_user(user_id)

# Найдем список групп друзей пользователя
# def get_groups_friends(*args):
#     friends_id = get_friends(user_id)
#     print(friends_id)
#     # groups_id = [vkapi.groups.get(user_id=id, extended=0, count=1000, timeout=10) for id in friends_id]
#     # time.sleep(3)
#     for id in enumerate(friends_id):
#         groups_id = vkapi.groups.get(user_id=id, extended=0, count=1000, timeout=10)
#         time.sleep(1)
#         print(groups_id)
#
#     return groups_id
# get_groups_friends(friends_id)


# Опредлим, являются ли друзья пользователя членами сообществ пользователя
def get_is_members(*args):
    friends_id = get_friends(user_id)
    group_id_list = get_groups_user(user_id)
    group_id = '74404187'
    members = vkapi.groups.isMember(group_id=group_id, user_ids=friends_id, extended=1)
    # for group_id in group_id_list:
    # members = [vkapi.groups.isMember(group_id=group_id, user_ids=friends_id, extended=1) for group_id in group_id_list]
    time.sleep(1)
    print(members)

    '''
    Получим список словарей по каждому другу пользователя типа: 
    [{'member': 0, 'user_id': 8822}, {'member': 1, 'user_id': 20338},...{}]
    Требуется исключить из списка друзей, которые не являются членами группы пользователя ({'member': 0}), 
    т.е. в список добавляем словари, в которых {'member': 1}.
    '''
    friends_in_groups = [friend for friend in members if friend['member'] == 1]
    print(friends_in_groups)

    return members


get_is_members(friends_id)

# def main():
#     user_id = input('Введите id или ссылку на страницу пользователя (в конце добавьте пробел): \n')
#     user_id = get_user_id(user_id)
#     print(f'Идентификатор пользователя: id = {user_id}')
#
#
#
#
# main()
