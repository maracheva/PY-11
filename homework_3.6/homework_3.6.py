# coding: utf-8

import requests
import os
import osa

GET_STATISTICS_URL = 'http://www.webservicex.net/Statistics.asmx?WSDL'  # URL расчета среднего значения
CONVERT_TEMP_URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'  # URL конвертора температуры
CONVERT_CURRENSY_URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL' # URL конвертора валюты
CONVERT_LENGTH_URL = 'http://www.webservicex.net/length.asmx?WSDL'

original_dir = 'currencies'  # папка с исходными файлами
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории
abs_dir = os.path.join(current_dir, original_dir)  # переменная = соединению путей рабочей директории

# Задание 1.  Вывести среднюю за неделю арифметическую температуру по Цельсию.
# Функция открывает файл на чтение и возвращает список значений температуры
def get_temperatures(file_name):
    with open(os.path.join(abs_dir, file_name)) as file:
        return [int(temperature.split()[0]) for temperature in file]

# Находим среднее занчение с помощью сервера http://www.webservicex.net/New/Home/ServiceDetail, получаем список
# def get_average(arg1, arg2):
#     client = osa.Client(GET_STATISTICS_URL)  # Клиент инициализируется полным адресом документа WSDL 1.1:
#     response = client.service.GetStatistics(arg1, arg2)
#     return response.Average

# Функция расчета среднего значения температуры по Фаренгейту
def get_average(temperature):
    avgarage_temp = sum(temperature) / (len(temperature))
    return avgarage_temp

# Функция конвертации температуры из Фаренгейтов в Цельсии
def convert_temperature(temperature):
    client = osa.Client(CONVERT_TEMP_URL)
    return client.service.ConvertTemp(temperature, 'degreeFahrenheit', 'degreeCelsius')

# Функция получения среднего значения температуры в Цельсиях
def get_average_temperature(file_name):
    temperatures = get_temperatures(file_name)
    average_temp = get_average(temperatures)
    celsius_temp = convert_temperature(average_temp)
    return '{:.2f}'.format(celsius_temp)

# Задание 2. Посчитать, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).
# Функция конвертации стоимости за каждый перелет в рубли. Возвращает список в рублях:
def convert_currency(currency, cost):
    client = osa.Client(CONVERT_CURRENSY_URL)
    return client.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB', amount=cost, rounding=True)


# Функция открывает файл на чтение и возвращает список списков каждого перелета.
# Получим список [['MOSCOW-LONDON:', '120', 'EUR'], ['LONDON-NEWYORK:', '235', 'USD']...]
def get_fly_list(file_name):
    with open(os.path.join(abs_dir, file_name)) as file_cur:
        fly_list = [item.strip().split(' ') for item in file_cur]
        return fly_list


# Функция возвращает список стоимости перелетов в рублях.
# Получим список [8502, 13484, 1958, 2198, 5, 116, 19526]
def get_fly_list_rubles(currency):
    fly_list_rubles = []
    [fly_list_rubles.append(round(convert_currency(course[2], course[1]))) for course in currency]
    return fly_list_rubles


# Задание 3. Необходимо посчитать суммарное расстояние пути в километрах с точностью до сотых.
# Функция конвертации расстояния из милей в километры
def convert_length(length):
    client = osa.Client(CONVERT_LENGTH_URL)
    length = client.service.ChangeLengthUnit(length, 'Miles', 'Kilometers')
    return length

# Функция открывает файл на чтение и возвращает сумму расстояний пути в км
def get_length_in_km(file_name):
    with open(os.path.join(abs_dir, file_name)) as file_len:
        length_list = [float(length_sum.split(' ')[1].replace(',', '')) for length_sum in file_len]
        # print(*length_list)
        # Получим список вещественных чисел из исходного файла:
        # [1,553.86 3,461.17 4,051.43 10,527.11 591.68 2,910.57 2,697.52]
        # В форме записи каждого числа есть запятая, разделяющая сотую чать, и точка, разделяющая
        # дробную часть. Требуется убрать запятую (replace(',', '')
        # и объединить через пробел все значения расстояний split('')[1].
        # Раз список состоит из вещественных чисел, необходимо добавить float(), т.к. операция сложения
        # выполняется только для целых чисел.
        length_sum = convert_length(sum([length_sum for length_sum in length_list]))
        return length_sum


def main():
    averange_temterature = get_average_temperature('temps.txt')
    print(f'1. Средняя температура в Цельсиях: {averange_temterature}')
    print('Подождите. Идет обработка...')
    amount_in_rubles = sum(get_fly_list_rubles(get_fly_list('currencies.txt')))
    print(f'2. Итоговая стоимость путешествия {amount_in_rubles} руб.')
    length_in_km = get_length_in_km('travel.txt')
    print(f'3. Cуммарное расстояние пути {length_in_km:.2f} км.')


main()