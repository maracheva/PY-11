# coding: utf-8

import pep8 as pep8

import os

migrations = 'Migrations'  # папка с данными
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории текущего файла
abs_dir = os.path.join(current_dir, migrations)  # переменная = соединению путей текущего файла и папки с данными

# Функция возвращает список sql-файлов в директории:
def files_reader():
    all_files = os.listdir(abs_dir)  # переменная = списку файлов и папок в рабочей директории
    return [file_name for file_name in all_files if '.sql' in file_name]
# file_name - файл данных, в котором нужно искать

# Функция поиска слова в файле:
def search_word(file_name, word, abs_dir):
    with open(os.path.join(abs_dir, file_name), 'r', encoding='utf-8') as f:
        # word = f.read() # читаем файл
        # return word
        return word in f.read()
# os.path.join(abs_dir, file_name - соединяем абсолютный путь рабочей директории с файлом данных
# word - слово, которое нужно искать

# Функция фильтрует список файлов по искомому слову и возвращает отфильтрованный список файлов.
def search_files(files_list, word, abs_dir=''):
    new_files_list = []
    for file_name in files_list:
        if search_word(file_name, word, abs_dir):
            new_files_list.append(file_name)
    return new_files_list


if __name__ == '__main__':
    abs_dir = os.path.join(current_dir, migrations)
    files = files_reader()
    while True:
        word = input('Введите строку: ')
        files = search_files(files, word, abs_dir)
        print('\n'.join(files))
        result_len = len(files)
        print('Всего: {}'.format(result_len))

# if __name__ == '__main__':
#     with open(abs_dir) as file:
#         print(file.read())
#     # ваша логика
#     pass
