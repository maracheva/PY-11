# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:
documents = [
        {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
        {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
        {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
      ]
    
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

#Задание 1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

# 1.1
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def name_by_number():
  number_doc = input ('Введите номер документа')
  i = 0
  for document in documents:
    i += 1
    if document['number'] == number_doc:
      print ('Номер документа введен верно. Владелец документа: {}'.format(document['name']))
      break
    elif i == len(documents):
      print ('Такого номера документа нет в базе.')
      name_by_number()
  # else:
  #   print ('Такого номера документа нет в базе.')
      
#name_by_number()

# 1.2
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_doc():
  for documents_list in documents:
    print('{} "{}" "{}" '. format(documents_list['type'], documents_list['number'], documents_list['name'])) 
#list_doc()  

# 1.3
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def shelf_by_number():
  number_doc = input('Введите номер документа:')
  i = 0
  for directory in directories.items():
    i += 1
    if number_doc in directory[1]:
      print('Документ "{}" находится на полке "{}"'.format(number_doc, directory[0]))
      break
    elif i == len(directories):
      print('Документ "{}" на полках не найден'.format(number_doc))
      shelf_by_number()
#shelf_by_number()

# 1.4
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add_doc():  
  input_type = input('Введите тип документа:')
  input_number = input('Введите номер документа:')
  input_name = input('Введите имя владельца документа:')
  input_shelf = input('Введите номер полки:')
  new_dict = dict(type = input_type, number = input_number, name = input_name)
  documents.append(new_dict)
  print('Документ добавлен в каталог:\n {} {} {}'.format(new_dict['type'], new_dict['number'], new_dict['name']))
  # Добавим номер полки, где будет храниться новый документ
  for directory in directories.items():
    if directory[0] == input_shelf:
       directory[1].extend(input_number) # расширяет список directory, добавляя в конец все элементы списка
    else:
      new_dict = directories.copy()
      new_dict[input_shelf] = input_number
  # print(new_dict)
  print('Номер полки:\n {}'.format(input_number))
#add_doc()  

# Задача №2. Дополнительная (не обязательная)
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def delete_doc():
  number_doc = input('Введите номер документа который хотите удалить:')
  for document in documents:
    if document['number'] == number_doc:
      document.clear() # очистим список
      for directory in directories.items():
        if number_doc in directory[1]:
          directory[1].remove(number_doc) # удаляет первый элемент в списке, имеющий значение number_doc
          # print(documents, directories)
          print('Документ "{}" успешно удален.'.format(number_doc))
      break    
  else:
    print('Документ с таким номером не найден, попробуйте ещё раз.')
    delete_doc()
#delete_doc()         

# Вывод пользовательских программ на экран:          
def print_func():
  print('Выберите одну из команд: \n'
  'p - Узнать кому принадлежит документ; \n'
  'l - Вывести список документов в формате "passport "2207 876234" "Василий Гупкин"; \n'
  's - Узнать номер полки, на которой хранится документ; \n'
  'a - Добавить новый документ; \n'
  'd - Удалить документ из каталога и из перечня полок; \n')

  user_input = input('Введите вариант ответа (p, l, s, a, d): ')
  if user_input == 'p':
    name_by_number()
  elif user_input == 'l':
    list_doc()
  elif user_input == 's':
    shelf_by_number()
  elif user_input == 'a':
    add_doc()
  elif user_input == 'd':
    delete_doc()
  else:
    print('Введено недопустимое значение, попробуйте ещё раз.')

print_func()

# options = ["p", "l", "s", "a", "d", "q", "?"]
# choice = input("Введите одно из значений (p, l, s, a, d), 'q' для выхода, или '?' для справки:")
# if choice in options:
#     if choice == "p":
#         print("\nПоиск пользователя по номеру документа:")
#         name_by_number()
#     if choice == "l":
#         print("\nПолный список документов:")
#         list_doc()
#     if choice == "s":
#         print("\nПоиск полки по номеру документа:")
#         shelf_by_number()
#     if choice == "a":
#         print("\nДобавление нового документа:")
#         add_doc()
#     if choice == "d":
#         print("Удаление документа из каталога и из перечня полок:")
#         delete_doc()
#     # if choice == "m":
#     #     print("Перемещение документа:")
#     #     name_by_number()
#     # if choice == "as":
#     #     print("Добавление новой полки:")
#     #     name_by_number()
#     elif choice == "q":
#         print("Работа завершена.")
#     elif choice == "?":
#         print("p - поиск пользователя по номеру документа,\n"
#         "l - список документов,\n"
#         "s - поиск полки по номеру документа,\n"
#         "a - добавление нового документа,\n"
#         "d - удаление документа")
# else:
#     print("Введено недопустимое значение, попробуйте ещё раз.")
