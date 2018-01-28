# coding: utf-8
# pip3 install chardet

import chardet


# фукнция чтения и сортировки файлов
def word_sort(name):
    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        all_text = data.decode(result['encoding'])

        words_list = all_text.split(' ')  # разделяем список пробелами
        word_value = {}  # формируем словарь {слово:количество}
        for word in words_list:  # ищем слова word > 6 символов в списке
            if len(word) > 6:
                word = word.lower()
                if word in word_value:  # для подсчета слов, достаточно проверить есть ли слово в word_value или нет.
                    word_value[word] += 1  # если есть, то увеличиваем на единицу
                else:
                    word_value[word] = 1  # если нет, то задаем значение = 1

        # Сортируем пары (слово, частота) по частоте, т.е. по x[1]
        # reverse=True даст отсортированные пары по убыванию
        sorted_count_pairs = sorted(word_value.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_count_pairs[:10]  # Берем первые 10 штук
        for i, (word, freq) in enumerate(top10):  # выведем на экран пронумерованный список ТОП10 слов
            print('{:>2}. Слово "{}" встретилось {} раз'.format(i + 1, word, freq))


# главная функция: запрашивает имя файла, запускает другие функции
def main():
    while True:
        name_number = input('\n1 - newsafr.txt'
                            '\n2 - newscy.txt'
                            '\n3 - newsfr.txt'
                            '\n4 - newsit.txt'
                            '\nВыход - exit. '
                            '\nВведите 1, 2, 3 или 4, exit: ')
        print('...Идет обработка')
        if name_number == '1':
            name = 'newsafr.txt'
            word_sort(name)
        elif name_number == '2':
            name = "newscy.txt"
            word_sort(name)
        elif name_number == '3':
            name = 'newsfr.txt'
            word_sort(name)
        elif name_number == '4':
            name = 'newsit.txt'
            word_sort(name)
        elif name_number == 'exit':
            break
        else:
            print('Некорректный ввод. Повторите.')


main()
