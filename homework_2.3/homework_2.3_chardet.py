# coding: utf-8
# import pep8 as pep8

import json
import chardet

# Запишем все файлы json, которые нужно отсортировать, в список словарей:
files = [{'name': 'newsafr.json', 'encoding': 'utf-8'}, {'name': 'newscy.json', 'encoding': 'koi8_r'},
    {'name': 'newsfr.json', 'encoding': 'cyrillic'}, {'name': 'newsit.json', 'encoding': 'cp1251'}]


def word_sort():
    for news_text in files:
        with open(news_text['name'], 'rb') as file:
            data = file.read()
            result = chardet.detect(data)
            news = data.decode(result['encoding'])
            news = json.loads(news)  # зададим переменную news и загрузим файлы с текстом

        # Добавим новый словарь, куда будем записывать слова > 6 символов.
        words = {}
        for item in news['rss']['channel']['items']:
            for word in item['description'].split() and item['title'].split():
                if len(word) > 6:
                    word = word.lower()
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
        # Сортируем пары (слово, частота) по частоте, т.е. по x[1]
        # reverse=True даст отсортированные пары по убыванию
        sorted_count_pairs = sorted(words.items(), key=lambda x: x[1], reverse=True)
        top10 = sorted_count_pairs[:10]  # Берем первые 10 штук
        print('\n{:-^50}'.format(news_text['name']))
        for i, (word, freq) in enumerate(top10):  # выведем на экран пронумерованный список ТОП10 слов
            print('{:>2}. Слово "{}" встретилось {} раза'.format(i + 1, word, freq))


word_sort()

# 'rss' - ключ основного словаря, который состоит из других словарей.
# 'channel' - ключ словаря 'rss'.
# 'items' - ключ словаря 'channel'.
# 'description' - ключ списка словарей в 'items'.
# 'title' - ключ списка словарей в 'items'. По ключу 'title' можно не делать поиск,
# т.к. title является заголовком, т.е. краткой выжимкой из основного текста discription.
# Остальные ключи не содержат текст, поэтому не будем проводить по ним поиск слов.
