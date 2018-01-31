#coding: utf-8
from urllib.parse import urlencode
import requests

AUTH_URL = 'https://oauth.vk.com/authorize' # адрес авторизации
APP_ID = 6353308  # application ID

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends',
    'response_type': 'token',
    'v': 5.71
}
# client_id - идентификатор приложения;
# display - указывает тип отображения страницы авторизации (page — форма авторизации в отдельном окне);
# scope - битовая маска настроек доступа приложения;
# response_type	 - тип ответа, который необходимо получить. Укажите token.
# v	- версия API, которую Вы используете. Актуальная версия: 5.71.

print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = 'bfbf48c783b48e19572e65f39f2736601e84064017b741e43fe1c93e501e7f630e54f1dc2b39961533d79'

params = {
    # 'source_uid': user_id1,
    # 'target_uid': user_id2,
    # 'order': 'order',
    'v': 5.71,
    'access_token': TOKEN
          }
# метод friends.getMutual возвращает список идентификаторов общих друзей между парой пользователей.
# source_uid - ID пользователя, чьи друзья пересекаются с друзьями пользователя с ID target_uid.
# target_uid - ID пользователя, с которым необходимо искать общих друзей.
# target_uids - список идентификаторов пользователей, с которыми необходимо искать общих друзей.
# order - порядок, в котором нужно вернуть список общих друзей (random - возвращает друзей в случайном порядке)
#  По умолчанию — в порядке возрастания идентификаторов.


def get_mutural_friends(user_id1, user_id2):
    if (user_id1, user_id2) in params:
        params['user_id1'] = user_id1
        params['user_id2'] = user_id2
    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    print(response.json()['response'])

user_id1 = input('Введите id первого пользователя: ')
user_id2 = input('Введите id второго пользователя: ')
get_mutural_friends(user_id1, user_id2)

def get_status(user_id=None):
    if user_id:
        params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/status.get', params)
    print(response.json())

get_status()

# Функция получения списка друзей
def get_friends(user_id):
    """
    user_id - идентификатор пользователя, для которого необходимо получить список друзей.
    """
    if user_id:
        params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    # return response.json()['response']['items']
    print(response.json())

get_friends(user_id)