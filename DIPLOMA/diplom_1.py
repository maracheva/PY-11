# coding: utf-8

import time
import json
import requests


# TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'
TOKEN = '341f7743773a83ad6d50b04d624d61ba46fc8c9f2df7d74d45c245bfe6628a5b26e0aac0d0b1083fc3719'
# TOKEN = 'f06bf1792fa30f3f16841177882498b0e32e3fc57161de4b70eebfd35f4127ad243267fa721f3bb4c0e07'

api_v = 5.73
APP = 6413027  # application ID

auth_data = {
    'client_id': APP,
    'display': 'page',
    'scope': 'status, friends, groups',
    'response_type': TOKEN,
    'v': api_v
}


'''
В качестве входных данных будет выступать ссылка на профиль пользователя. 
Нам понадобится цифровой id, который не всегда в ней указан,  
Поэтому с помощью метода utils.resolveScreenName мы получаем что нам нужно.
'''
link = 'https://vk.com/tim_leary'  # ссылка на страницу пользователя
# user_id = '5030613'


# Функция получает id пользователя и возвращает его значение
def get_user_id(*args):
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


user_id = get_user_id(link)


# 1. Функция поиска друзей методом friend.get.
# Возвращает список идентификаторов друзей пользователя и расширенную информацию по параметру fields.
def get_friends(*args):
    params = {
        'user_id': user_id,
        'fields': 'status',
        'v': api_v
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends = response.json()['response']
    print(f"Количество друзей пользователя: {friends.get('count')}")
    '''
    1. Функция get_friends(*args) находит всех друзей пользователя по методу friend.get.
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
    '''
    friends_status = [friend for friend in friends['items'] if ('status') in friend]
    friends_deactiv = [friend for friend in friends['items'] if friend.get('deactivated')]
    # print(f'Количество друзей в активном статусе: {len(friends_status)}')
    # print(f'Количество друзей удаленных или забаненных: {len(friends_deactiv)}')

    # Из списка друзей friends_status получим список только с id друзей пользователя:
    friends_id_list = [friend.get('id') for friend in friends_status]

    return friends_id_list


friends_id = get_friends(user_id)


# 2. Функция находит  и возвращает список групп пользователя по id.
# Будем находить группы методом groups.get. Параметр extended=1 позволяет получить расширенную информацию о группе.
def get_groups_user(*args):
    params = {
        'user_id': user_id,
        'extended': '1',
        'fields': 'members_count',
        'access_token': TOKEN,
        'v': api_v
    }
    response = requests.get('https://api.vk.com/method/groups.get', params, timeout=10)
    groups = response.json()['response']
    # Получили словарь типа {'count': int, 'items': [{}, {}, ..., {}]}
    print(f"Количество групп пользователя: {groups.get('count')}")
    # Запишем в отдельный список полученные данные по группам.
    groups_list = groups.get('items')
    print(groups_list)
    return groups_list

get_groups_user(user_id)


# 3. Функция возвращает список id групп:
def get_groups_user_id(*args):
    params = {
        'user_id': user_id,
        'extended': '0',
        'access_token': TOKEN,
        'v': api_v,
    }
    # Получим словарь только с id групп пользователя:
    response = requests.get('https://api.vk.com/method/groups.get', params, timeout=10)
    groups_id = response.json()['response']
    # Генератор списка id групп пользователя:
    groups_id_list = [id for id in groups_id['items']]
    return groups_id_list

print(get_groups_user_id(user_id))

# Функция разбивает список на список списков по 24 элемента в каждом
split_by_10 = lambda lst, sz: [lst[i:i + sz] for i in range(0, len(lst), sz)]
split_by = split_by_10(friends_id, 24)
print(len(split_by))

#  Метод groups.getMembers
def get_members():
    group_id_list = get_groups_user_id(user_id)
    friends_id = get_friends(user_id)
    token = TOKEN
    url = "https://api.vk.com/method/execute?"

    groups_without_friends = {}
    all_members = []
    for group_id in group_id_list:
        CODE = '''
        var i = 0;
        var members = [];
        var offset = 0;
        while(i < 2){
        var resp = API.groups.getMembers({
                        "group_id": %s, 
                        "offset": offset, 
                        "filter": "friends"
        });
        members.push(resp);
        i = i + 1;
        offset = offset + 1000;
        }
        return members;
        ''' %(group_id)

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        time.sleep(1)
        members = response_data['response']
        for element in members:
            if element['count'] == 0:
                print(element['count'])
                all_members.append(members)
        print(all_members)


    return all_members


get_members = get_members()
print(len(get_members))

# Опредлим, являются ли друзья пользователя членами сообществ пользователя
def get_is_members(*args):
    friends_id = get_friends(user_id)
    group_id_list = get_groups_user_id(user_id)

    # Метод execute:
    token = TOKEN
    url = "https://api.vk.com/method/execute?"

    groups_without_friends = {}
    all_members = []
    for group_id in group_id_list:

        CODE = '''
        var group_id = Args.group_id;
        var user_ids = Args.user_ids;
        var members = API.groups.isMember(
                                    {"group_id": %s,
                                    "user_ids": %s,
                                    "extended":"1",
                                    "v":"5.73"});

        return members;
        '''%(group_id, friends_id)

        data = dict(code=CODE, access_token=token, v=api_v)
        execute = requests.post(url=url, data=data, timeout=10)
        response_data = execute.json()
        time.sleep(1)
        # print(response_data['response'])
        # print(f"Группа {group_id} метод execute: {response_data['response']}")

        '''
        Получили список словарей по всем друзьям для каждого id группы:
        [{'member': 0, 'user_id': 8822}, {'member': 0, 'user_id': 20338},...]
        Добавим в полученный список response_data['response'] словарь {'group_id': group_id}.
        Получим список типа [{'group_id': 47465154}, {'member': 0, 'user_id': 8822},..]
        response_data['response'].insert(0, {'group_id': group_id})
        '''
        # group_is_members = {
        #     'group_id': group_id,
        #     'friends':  response_data['response']
        # }
        # print(group_is_members)

        # all_members.append({'group_id': group_id})
        # all_members.append(response_data['response'])
        # all_members.reverse(response_data['response'])

        # Исключим тех друзей, которые состоят в группах пользователя ('member': 1).
        # for group_id in response_data['response']:
        #     if not(group_id['member'] == 0):
        #         all_members.append(response_data['response'])

        # if not (['member'] == 1) in group_is_members['friends']:
        #     all_members.append(group_is_members)

        # all_members = [group_is_members if not {'member': 1} in group_is_members.get('friends')]

        # Исключим тех друзей, которые состоят в группах пользователя ('member': 1).
        # all_members = [response_data['response'] for element in response_data['response'] if not (element.get('member') == 1)]
        # all_members = response_data['response']
        # print(all_members)

    return all_members


all_members = get_is_members()
print(f'Количество групп: {len(all_members)}')
print(f'Метод execute по всем группам {all_members}')
#
#
# def get_groups_without_friends(*args):
#     # members = get_is_members()
#     '''
#     Получим список словарей по каждому другу пользователя типа:
#     [{'member': 0, 'user_id': 8822}, {'member': 1, 'user_id': 20338},...{}]
#     Требуется исключить из списка друзей, которые являются членами группы пользователя ({'member': 1}),
#     т.е. в список добавляем словари, в которых {'member': 0}.
#     '''
#     friends_out_groups = [all_members for friend in friends_id if not (['member'] == 1)]
#     print(friends_out_groups)
#     print(len(friends_out_groups))
#
#     return friends_out_groups
#
# groups_without_friends = get_groups_without_friends()
# print(len(groups_without_friends))

# def groups_result():
#     groups_list_out = []
#     for group in groups_list:
#         groups_list_out.append({
#             'name': group.get('name'),
#             'gid': group.get('id'),
#             'members_count': group.get('members_count')
#          })
#     print(groups_list_out)
#     return groups_list_out


# # Функция выводит результат обработки запроса и показывает, сколько осталось до конца обработки:
# # def output_result(*args):
#
#
# # def main():
# #     user_id = input('Введите id или ссылку на страницу пользователя (в конце не забудьте пробел): \n')
# #     user_id = get_user_id(user_id)
# #     print(f'Идентификатор пользователя: id = {user_id}')
# #
# #     groups_list = get_groups_user(user_id)
# #     with open('groups.json', 'w', encoding='utf-8') as fw:
# #         data = groups_list
# #         json.dump(data, fw, sort_keys=True, indent=2, ensure_ascii=False)
# # #       output_result('Запись в файл завершена')
# # #
# # main()