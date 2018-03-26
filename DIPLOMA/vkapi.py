
from urllib.parse import urlencode
import requests

AUTH_URL = 'https://oauth.vk.com/authorize'  # адрес авторизации
APP_ID = 6413027  # application ID

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'status, friends, groups',
    'response_type': 'token',
    'v': 5.73
}
# client_id - идентификатор приложения;
# display - указывает тип отображения страницы авторизации (page — форма авторизации в отдельном окне);
# scope - битовая маска настроек доступа приложения;
# response_type	 - тип ответа, который необходимо получить. Укажите token.
# v	- версия API, которую Вы используете. Актуальная версия: 5.71.

print('?'.join((AUTH_URL, urlencode(auth_data))))
TOKEN = 'cd549f8ad69255caa1c37c00a3afbc541d8bc21a8ff70ad656a3441c7d4f13f9c0eca306542f4217fa6a7'
