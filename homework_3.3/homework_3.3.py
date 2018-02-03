# coding: utf-8

import requests
import os


def translate_it(text, lang):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.-
    :return: <str> translated text.
    """
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {'key': KEY,
              'lang': lang,
              'text': text
              }
    #print(params)
    response = requests.get(URL, params=params).json()
    #print(response)
    return ' '.join(response.get('text', []))

original_dir = 'Original'  # папка с исходными файлами с данными
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории
abs_dir = os.path.join(current_dir, original_dir)  # переменная = соединению путей рабочей директории
files_list = os.listdir(abs_dir)  # переменная = списку файлов в рабочей директории файла и файлов с данными .txt.

# Функция возвращает список txt-файлов в рабочую директорию:
def get_files_list():
    return [file for file in files_list if
            file.endswith('.txt')]  # находим файлы с .txt и помещаем их в список files_list

# Функция получает именя директорий исходных файлов и производит преобразование файлов в новые с другими размерами
def get_new_files():
    lang_ru = 'ru'
    if result_dir not in os.listdir():
        os.mkdir(result_dir)
    for file in os.listdir(original_dir):
        source_file = os.path.join(original_dir, file)
        #print(file) # выведет название файла DE.txt, ES.txt, FR.txt
        with open(source_file, 'r', encoding='utf8') as fr:
            lang_from = file[:2].lower() # сделаем ниж.регистр и срез (DE.txt[:2] или DE.txt[:-4])=DE, убираем (.txt)
            #print(lang_from)
            text_translated = translate_it(fr.read(), '{}-{}'.format(lang_from, lang_ru))
            result_file = os.path.join(result_dir, file)
        with open(result_file, 'w', encoding='utf8') as fw:
            fw.write(text_translated)


result_dir = 'Result'
get_new_files()
