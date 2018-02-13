#coding: utf-8

import requests
import requests
import os
import osa

ORIGINAL_DIR = 'currencies' # папка с исходными файлами
GET_STATISTICS_URL = 'http://www.webservicex.net/Statistics.asmx?WSDL'
CONVERT_TEMP_URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'  # URL конвектора температуры


# Задание 1.  Вывести среднюю за неделю арифметическую температуру по Цельсию.
# Находим среднее занчение, получаем список
def get_average(args):
    client = osa.Client(GET_STATISTICS_URL)
    array = client.types.ArrayOfDouble()
    array.double = args
    response = client.service.GetStatistics(array)
    return response.Average

# Функция конвертации температуры из Фаренгейтов в Цельсии
def convert_temperature(temperature):
    client = osa.Client(CONVERT_TEMP_URL)
    return client.service.ConvertTemp(temperature, 'degreeFahrenheit', 'degreeCelsius')


def get_temperatures(file_name):
   with open(os.path.join(ORIGINAL_DIR, file_name)) as f_temp:
        return [int(temperature.split()[0]) for temperature in f_temp]


def get_average_temperature(file_name):
    temperatures = get_temperatures(file_name)
    average_temp = get_average(temperatures)
    celsius_temp = fahrenheit_to_celsius(average_temp)
    return '{:.2f}'.format(celsius_temp)

print('1. Средняя температура в Цельсиях: {}\n'.format(get_average_temperature('temps.txt')))
