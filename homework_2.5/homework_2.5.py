# coding: utf-8

import subprocess
import os


# Функция, которая получает файлы из рабочей директории (относит.путь) и возвращает список этих файлов
def get_files_list(source_dir):
    return [image for image in os.listdir('Source') if image.endswith('.jpg')]


# Функция получает именя директорий исходных файлов и производит преобразование файлов в новые с другими размерами
def resizer(source_dir, output_dir):
    if output_dir not in os.listdir(): # если output_dir нет в списке файлов рабочей директории, то создать папку.
        os.mkdir(output_dir)            # создать папку output_dir
    for image in get_files_list(source_dir):
        source_image = os.path.join(source_dir, image)
        output_image = os.path.join(output_dir, image)
        # subprocess.run(['convert', source_image, '-resize', '200', output_image]) # синхронное выполнение
        subprocess.Popen(['convert', source_image, '-resize', '200', output_image]) # асинхронное выполнение

source_dir = 'Source'
output_dir = 'Result'
resizer(source_dir, output_dir)
