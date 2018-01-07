#coding: utf-8

#import requests
#
# cook_book = {'яйчница': [{'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#                          {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}],
#     'стейк': [{'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#                 {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#                 {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}],
#     'салат': [{'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#             {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#             {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#             {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}]}

def cook_book_funk():
    list_dish_name = []
    list_ingridient = []
    with open("menu.txt", encoding='utf8') as file:
        for ingredient in file:
            key = ingredient.strip().lower()
            cook_book[key] = []
            for _ in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                cook_book[key].append(
                    {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            file.readline()

    ingridient_dict = []
    for element in list_ingridient:
        dict_elem = []
        for elementen in element:
            cook_book_key = {}
            cook_book_key["ingridient_name"] = elementen[0]
            cook_book_key["quantity"] = int(elementen[1])
            cook_book_key["measure"] = elementen[2]
            dict_elem.append(cook_book_key)
        ingridient_dict.append(dict_elem)
    ingridients_dict = dict()
    count = 0
    for elem in list_dish_name:
        ingridients_dict[elem] = ingridient_dict[count]
        count += 1
    #return (ingridients_dict)
    cook_book[dish] = ingredients_dict
    return cook_book



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']


    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()

