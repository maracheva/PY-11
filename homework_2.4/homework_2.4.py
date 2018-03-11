import os

migrations = 'Migrations'  # папка с данными
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории текущего файла
abs_dir = os.path.join(current_dir, migrations)  # переменная = соединению путей текущего файла и папки с данными


# Функция возвращает список sql-файлов в директории:
def files_reader():
    all_files = os.listdir(abs_dir)  # переменная = списку файлов и папок в рабочей директории
    return [file for file in all_files if file.endswith('.sql')]

# Функция поиска слова в файле.
def search_word(file, word):
    with open(os.path.join(abs_dir, file), 'r', encoding='utf-8') as fp:
        # for line in iter(fp.readline, ''):      # читаем из файла до первой пустой строки
        #     if word in line:                    # если слово есть в сторке, возвращаем его
        #         return word
        return [word for line in iter(fp.readline, '') if word in line]

# Функция фильтрует список файлов по искомому слову и возвращает отфильтрованный список файлов.
def search_files(files_list, word):
    new_files_list = [file for file in files_list if search_word(file, word)]
    return new_files_list

'''
Реализзовать логику по хранению предыдущего шага. 
Храниться будет только 1 шаг. Если пользователь в качестве слова для поиска введет "go back", 
программа должна распечатать файлы с предыдущего шага и предложить поискать в них.
'''
# Функция возвращает список списка файлов, найденных по слову  word
def keep_on_step(files_list, word):
    search_history = []
    new_files_list = search_files(files_list, word)
    for file in new_files_list:
        search_history.append(file)
    return search_history


def main():
    files = files_reader()
    while True:
        word = input('Введите строку: ')
        print('...Идет обработка файлов')

        files = search_files(files, word)
        print('\n'.join(files))
        print(f'Всего найдено файлов: {len(files)}')

        files_step = keep_on_step(files, word)
        user_input = input('''
        Для просмотра последнего файла введите go back
        Для продолжения поиска слова, введите исходное слово
        Введите строку:
        ''')
        print('...Идет обработка')
        if user_input == 'go back':
            print(f'Последний файл: {files_step[-1]}')   # распечатывает последний шаг - последний файл
            print(f'Всего найдено файлов: {len(files_step)}')
            print(f'Последний файл (метод pop()): {files_step.pop()}')  # распечатывает последний файл и удаляет его
            print(f'{len(files_step)}\n')
        elif user_input == word:
            new_files_list = [file for file in files_step]
            print('\n'.join(new_files_list))
            print()
        else:
            print('Некорректный ввод. Повторите.')

main()
