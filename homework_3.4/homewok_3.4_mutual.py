# coding: utf-8

import requests

TOKEN = 'bfbf48c783b48e19572e65f39f2736601e84064017b741e43fe1c93e501e7f630e54f1dc2b39961533d79'


def get_mutural_friends(user_id1, user_id2):
    params = {
        'source_uid': user_id1,
        'target_uid': user_id2,
        'access_token': TOKEN
    }

    if (user_id1, user_id2) in params:
        params['source_uid'] = user_id1
        params['target_uid'] = user_id2
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    print('Список индефикаторов общих друзей: ', response.json()['response'])

    for i, user_id in enumerate(response.json()['response']):
        print(f'{i+1}. Ссылка на страницу общего друга {user_id}: https://vk.com/id{user_id}')


user_id1 = input('Введите id первого пользователя: ')  # 2125612
user_id2 = input('Введите id второго пользователя: ')  # 1307803

get_mutural_friends(user_id1, user_id2)

# метод friends.getMutual возвращает список идентификаторов общих друзей между парой пользователей.
# source_uid - ID пользователя, чьи друзья пересекаются с друзьями пользователя с ID target_uid.
# target_uid - ID пользователя, с которым необходимо искать общих друзей.
# target_uids - список идентификаторов пользователей, с которыми необходимо искать общих друзей.
# order - порядок, в котором нужно вернуть список общих друзей (random - возвращает друзей в случайном порядке)
#  По умолчанию — в порядке возрастания идентификаторов.
