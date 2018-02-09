# coding: utf-8

import requests
from urllib.parse import urlencode
from pprint import pprint

APP_ID = '60bc32e7cd3246ad99572a7d217948e5'  # ID созданного приложения
AUTH_URL = 'https://oauth.yandex.ru/authorize'  # url авторизации для запроса токена

auth_url_data = {'response_type': 'token', 'client_id': APP_ID}
print('?'.join((AUTH_URL, urlencode(auth_url_data))))

TOKEN = 'AQAAAAAiVObAAATMJ2ugYfyDVE32qQ7iYzH1W0s'


class YandexMetrikaUser(object):
    token = None

    def __init__(self, token):
        self.token = token

    @property
    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }

    @property
    def counter_list(self):
        headers = self.get_headers
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', headers=headers,
                                params={'pretty': 1})
        counters = response.json()['counters']
        counter_list = [counter['id'] for counter in counters]
        # return [counter['id'] for counter in counters]
        return counter_list

    def get_counter_info(self, token, counter_id):
        headers = self.get_headers
        self.counter_id = counter_id
        self.token = token
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits, ym:s:pageviews, ym:s:users'  # кол-во визитов, просмотров, посетителей
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params, headers=headers)
        info_count = response.json()['totals']
        # return [visits['data'] for visits in visits_count]
        return info_count


my_token = YandexMetrikaUser(TOKEN)
# получим id приложения
counters = my_token.counter_list
pprint(counters)
# получим список из числа визитов, кол-ва просмотров и числа посетителей
info = my_token.get_counter_info(TOKEN, '47584465')
pprint(info)
