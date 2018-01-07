#coding: utf-8

import chardet as ch

def words_count(article):
    with open(article, "rb") as news:
        data = news.read()
        result = ch.detect(data)
        full_text = data.decode(result["encoding"])
        fields = full_text.split()

        long_words = []
        for words in fields:
            alfa = len(words)
            if alfa > 6:
                long_words.append(words.lower())

        words_with_count = {}
        count = 0
        for words in long_words:
            words_with_count[words] = count
        for key, values in words_with_count.items():
            for words in long_words:
                if key == words:
                    words_with_count[words] += 1

        count_list = []
        for value in words_with_count.values():
            if value not in count_list:
                count_list.append(value)
        beta = sorted(count_list)
        count_list_reverse = beta[::-1]

        count_list_reverse_lim = count_list_reverse[:10]

        for elementen in count_list_reverse_lim:
            for key, values in words_with_count.items():
                if words_with_count[key] == elementen:
                    print('Слово "{}" встречается {} раз(а)'.format(key, values))


def main():
    global article
    while True:
        article_number = input('Статьи:\n[1] = newsafr.txt\n'
                               '[2] = newscy.txt\n'
                               '[3] = newsfr.txt\n'
                               '[4] = newsit.txt\n'
                               'Введите номер статьи или любую другую кнопку для выхода: ')
        if article_number == "1":
            article = "newsafr.txt"
        elif article_number == "2":
            article = "newscy.txt"
        elif article_number == "3":
            article = "newsfr.txt"
        elif article_number == "4":
            article = "newsit.txt"
        else:
            break
        print("Топ 10 наиболее часто встречающихся слов длиннее 6-ти символов:")
        words_count(article)


main()
