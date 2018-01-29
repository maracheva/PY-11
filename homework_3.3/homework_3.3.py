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
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {'key': key,
              # 'lang': '{}' + '-ru'.format(lang_from),
              'lang': lang,
              'text': text
              }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


# a = translate_it('Привет')
# print(a)
original_dir = 'Original'  # папка с исходными файлами с данными
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории
abs_dir = os.path.join(current_dir, original_dir)  # переменная = соединению путей рабочей директории
files_list = os.listdir(abs_dir)  # переменная = списку файлов в рабочей директории файла и файлов с данными .txt.

# Функция возвращает список txt-файлов в рабочую директорию:
def get_files_list():
    return [file for file in files_list if
            file.endswith('.txt')]  # находим файлы с .txt и помещаем их в список files_list

print(get_files_list())
# get_files_list()
# Функция получает именя директорий исходных файлов и производит преобразование файлов в новые с другими размерами
def get_new_files():
    # if result_dir not in files_list:  # если result_dir нет в списке файлов рабочей директории, то создать папку.
    #     os.mkdir(result_dir)  # создать папку result_dir, куда будем записывать новые файлы после их перевода
    # for file_ in get_files_list():
    #     result_files = os.path.join(original_dir, file_)
    #     print(result_files)
    #     with open(result_files, 'r', encoding='utf8') as fr:
    #         lang_from = file_.lower()
    #         text_after = translate_it(fr.read(), '{}'.format(lang_from))
    #         with open(result_files, 'w', encoding='utf8') as fw:
    #             fw.write(text_after)
    lang_ru = 'ru'
    if 'results' not in os.listdir():
        os.mkdir('results')
    for fl_file in os.listdir(original_dir):
        source_file = os.path.join(original_dir, fl_file)
        with open(source_file, 'r', encoding='utf8') as f_read:
            lang_from = fl_file[:-4].lower()
            translated = translate_it(f_read.read(), '{}-{}'.format(lang_from, lang_ru))
            result_file = os.path.join('results', fl_file)
            with open(result_file, 'w', encoding='utf8') as f_write:
                f_write.write(translated)


result_dir = 'Result'
get_new_files()
