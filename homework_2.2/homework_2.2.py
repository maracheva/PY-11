#coding: utf-8
#pip3 install chardet

import chardet

# фукнция чтения файлов
def read_files(name):
    with open(name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        all_text = data.decode(result['encoding'])
        return all_text


# функция подсчета слов длиннее 6 символов
def count_word(all_text):
    to_list = all_text.split(' ')
    to_set = set()
    for i in to_list:  # заполняем множество словами > 6 символов
        if len(i) > 6:
            to_set.add(i)
    word_value = {}  # формируем словарь {слово:количество}
    for i in to_set:  # ищем слова из множества в списке, считаем количество
        count = 0     # введем переменную кол-во = 0
        for j in to_list:
            if i == j:
                count += 1
        word_value[i] = count
    return word_value  # возвращаем словарь {слово:количество}


# функция сортировки и вывода ТОП-10
def sort_top(word_value):
    register = [] # создадим новый список
    l_dict = str(len(word_value)) # введем параметр длины словаря = строке(длины (словаря кол-ва слов))
    for i in word_value.items():
        l_word = str(i[1])
        register.append((len(l_dict) - len(l_word)) * '0' + str(i[1]) + ' ' + i[
            0])  # разворачиваем и добавляем нули перед количеством для сортировки, делаем слияние элементов = '00012 слово'
    register.sort(reverse=True)
    top_10 = {} # новый словарь
    count = 1
    for j in register:
        top_10[count] = j.split(' ')  # получаем словарь типа {1: (количество, слово)}
        top_10[count][0] = int(top_10[count][0])
        if count == 10: # цикл, если кол-во = 10, завершение цикла
            break
        count += 1
    return top_10  # возвращаем отсортированный словарь ТОП-10 {номер: (количеств, слово)}


# главная функция: запрашивает имя файла, запускает другие функции
def main():
    while True:
        name = input('Введите имя файла: newsfr.txt, newsit.txt, newsafr.txt, newscy.txt. Выход - exit: ')
        if name == 'newsfr.txt' or name == 'newsit.txt' or name == 'newsafr.txt' or name == 'newscy.txt':
            print('Обработка файла ...')
            top_10 = sort_top(count_word(read_files(name)))
            for k in top_10.values():
                print('Слово "{}" = {} раз'.format(k[1], k[0]))
        elif name == 'exit':
            break
        else:
            print('Некорректный вводовторите.')


main()