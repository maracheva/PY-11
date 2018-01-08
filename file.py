# coding: utf-8

# В файле file.py создадим переменную path и укажим в ней путь к файлу menu.txt.
path = 'menu.txt'
# Создадим переменную menu_file и зададим в ней опцию open() и режим ‘r’, чтобы открыть файл menu.txt только для чтения.
# file = open(path, encoding = 'utf8')

def cook_book_collector():
    cook_book = {}
    with open(path, encoding = 'utf8') as file:
        for ingredient in file:
            dishes_file = file.readline() # читаем файл построчно
            dishes_file = ''.join(dishes_file.strip().split('|')) # убираем пустую строку и пробелы заменяем на разделитель
            key = ingredient.strip()
            cook_book[key] = [] # создаем пустой список блюд по ключам
            # dishes_list = []  # создаем пустой список блюд
            for key in dishes_file:

            # for key in dishes_file.keys():
                #key['ingredient'] == key[0]
                key['quantity'] == int(key[1])
                key['measure'] == key[2]
                cook_book[key].append({
                    'Название ингредиента': ingredient,
                    'Количество': int(quantity),
                    'measure': measure
                    })
            cook_book[dish] = ingredient_list
            print(ingredient_list)
            file.readline()
    return cook_book
cook_book_collector()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
    # person_count = int(input('Введите количество человек: '))
    person_count = 3
    # dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    dishes = 'стейк, салат'.lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

# Задача №2
# Напишите, для чего используются типы данных: json, xml, yaml.
# JSON (англ. JavaScript Object Notation) — текстовый формат обмена данными, основанный на JavaScript и обычно используемый именно с этим языком.
# Формат считается языконезависимым и может использоваться практически с любым языком программирования.
#  var earth =
# {
#  "planet" :
#  {
#   "name" : "earth",
#   "type" : "small",
#   "info":
#   [
#    "Earth is a small planet, third from the sun",
#    "Surface coverage of water is roughly two-thirds",
#    "Exhibits a remarkable diversity of climates and landscapes"
#   ]
#  }
#  };

# xml
# XML – это eXtensible Markup Language, что в переводе значит «расширенный язык разметки».
# Фактически, это способ записи данных в структурированном виде, который будет читаем для пользователя,
# но при этом удобен для обработки программному обеспечению. XML документ содержит один или более элементов,
#  разделённых открывающими и закрывающими тегами:

# <str>Hello!</str>

# YAML — легкочитаемый формат сериализации данных, концептуально близкий к языкам разметки,
# но ориентированный на удобство ввода-вывода типичных структур данных многих языков программирования.

# ---
#  -
#     - PRIVMSG
#     - newUri
#     - '^http://.*'
#  -
#     - PRIVMSG
#     - deleteUri
#     - ^delete.*
#  -
#     - PRIVMSG
#     - randomUri
#     - ^random.*