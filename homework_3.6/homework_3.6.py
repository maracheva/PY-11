# coding: utf-8

import requests
import os
import osa

GET_STATISTICS_URL = 'http://www.webservicex.net/Statistics.asmx?WSDL'  # URL расчета среднего значения
CONVERT_TEMP_URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'  # URL конвектора температуры

# Задание 1.  Вывести среднюю за неделю арифметическую температуру по Цельсию.
# Функция открывает файл на чтение и возвращает список значений температуры
original_dir = 'currencies'  # папка с исходными файлами
current_dir = os.path.dirname(os.path.abspath(__file__))  # имя абсолютного пути рабочей директории
abs_dir = os.path.join(current_dir, original_dir)  # переменная = соединению путей рабочей директории

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


def get_average_temperature(file_name):
    temperatures = get_temperatures(file_name)
    average_temp = get_average(temperatures)
    celsius_temp = convert_temperature(average_temp)
    return '{:.2f}'.format(celsius_temp)


averange_temterature = get_average_temperature('temps.txt')
print(f'1. Средняя температура в Цельсиях: {averange_temterature}')
