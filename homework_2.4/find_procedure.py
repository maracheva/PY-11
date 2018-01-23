# coding: utf-8

import pep8 as pep8

import os

migrations = 'Migrations'  # папка с данными
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории текущего файла
abs_dir = os.path.join(current_dir, migrations)  # переменная = соединению путей текущего файла и папки с данными

# Функция возвращает список sql-файлов в директории:
def files_reader():
    all_files = os.listdir(abs_dir)  # переменная = списку файлов и папок в рабочей директории
    return [file for file in all_files if file.endswith('.sql')]
# file - файл данных, в котором нужно искать

# Функция поиска слова в файле:
def search_word(file, word):
    with open(os.path.join(abs_dir, file), 'r', encoding='utf-8') as f:
     return word in f.read()
# os.path.join(abs_dir, file) - соединяем абсолютный путь рабочей директории с файлом данных
# word - слово, которое нужно искать

# Функция фильтрует список файлов по искомому слову и возвращает отфильтрованный список файлов.
def search_files(files_list, word):
    new_files_list = []
    for file in files_list:
        if search_word(file, word):
            new_files_list.append(file)
    return new_files_list


if __name__ == '__main__':
    files = files_reader()
    while True:
        word = input('Введите строку: ')
        print('...Идет обработка файлов')
        files = search_files(files, word)
        print('\n'.join(files))
        result_len = len(files)
        print('Всего: {}'.format(result_len))
