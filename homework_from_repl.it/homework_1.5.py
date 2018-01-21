# Имеется группа студентов, у каждого из которых есть следующие характеристики: имя, фамилия, пол, предыдущий опыт в программировании (бинарная переменная), 5 оцененных по 10-бальной шкале домашних работ, оценка за экзамен по 10-балльной шкале. Необходимо написать программу, которая в зависимости от запроса пользователя будет выводить:

# среднюю оценку за домашние задания и за экзамен по всем группе в следующем виде:
#         Средняя оценка за домашние задания по группе: X
#         Средняя оценка за экзамен: Y
# где X и Y - вычисляемые значения;
# среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта в виде:
#         Средняя оценка за домашние задания у мужчин: A
#         Средняя оценка за экзамен у мужчин: B
#         Средняя оценка за домашние задания у женщин: C
#         Средняя оценка за экзамен у женщин: D
        
#         Средняя оценка за домашние задания у студентов с опытом: E
#         Средняя оценка за экзамен у студентов с опытом: F        
#         Средняя оценка за домашние задания у студентов без опыта: G
#         Средняя оценка за экзамен у студентов без опыта: H
# где A, B, C, D, E, F, G, H - вычисляемые значения;
# определять лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.
# Студентов должно быть не менее 6. 
# Код должен быть грамотно декомпозирован (максимально используйте функции).

students = [
 
  {"name":"Valentina", "surname":"Tereshkova", "sex":"female", "experience":0, "homework": [10, 10, 10, 10, 9], "exam":10},
  
  {"name":"Yuriy", "surname":"Gagarin", "sex":"male", "experience":1, "homework": [10, 10, 9, 8, 10], "exam":10},
  
  {"name":"Elena", "surname":"Kondakova", "sex":"female", "experience":0, "homework": [10, 10, 10, 9, 10], "exam":10},
  
  {"name":"Yuriy", "surname":"Lonchakov", "sex":"male", "experience":1, "homework": [10, 10, 9, 10, 10], "exam":10},
  
  {"name":"German", "surname":"Titov", "sex":"male", "experience":0, "homework": [8, 8, 10, 9, 8], "exam":10},
  
  {"name":"Elena", "surname":"Kondakova", "sex":"female", "experience":1, "homework": [8, 9, 10, 9, 10], "exam":10}
]

# 1. Средняя оценка за домашние задания и за экзамен по всей группе:
# 1.1 Средняя оценка за домашние задания по группе:
# Функция расчета средней оценки группы за домашние задания:
def get_home_average_group():    
  average_home = (
    sum([sum(student["homework"]) / len(student["homework"]) for student in students]) / len(students))
  return average_home
average_home_group = get_home_average_group()
# print ("Средняя оценка за домашние задания по группе: %.2f" %average_home_group)

# 1.2 Средняя оценка за домашние задания по группе:
# Функция расчета средней оценки группы за экзамен:
def get_exam_average_group(): 
  average_exam = (sum([student["exam"] for student in students]) / len(students))
  return average_exam 
average_exam_group = get_exam_average_group()
# print("Средняя оценка за экзамен по группе: %.2f" %average_exam_group)

# 2. Расчет средней оценки за домашние задания и за экзамен по группе в разрезе: 
# а)пола
# Функция расчета средней оценки за домашние задания в зависимости от пола:
def get_home_average_sex(sex_gender):
  average = 0                                          
  quantity = 0 
  for student in students:
    if student["sex"] == sex_gender:
      average += sum(student["homework"])/len(student["homework"])
      quantity += 1 
  home_average_sex = average/quantity
  return home_average_sex
# Функция вывода на экран средней оценки за домашние задания у мужчин:
average_male = get_home_average_sex("male")
# print ("Средняя оценка за домашние задания у мужчин: %.2f" %average_male)
# Функция вывода на экран средней оценки за домашние задания у женщин:
average_female = get_home_average_sex("female")
# print ("Средняя оценка за домашние задания у женщин: %.2f" %average_female)

# Функция расчета средней оценки за экзамен в зависимости от пола:
def get_exam_average_sex(sex_gender):
  average_exam = 0                                          
  quantity = 0 
  for student in students:
    if student["sex"] == sex_gender:
      average_exam += student["exam"]
      quantity += 1 
  average_exam /= quantity
  return average_exam
# Функция вывода на экран средней оценки за экзамен у мужчин:
exam_male = get_exam_average_sex("male")
# print ("Средняя оценка за экзамен у мужчин: %.2f" %exam_male)
# Функция вывода на экран средней оценки за экзамен у женщин:
exam_female = get_exam_average_sex("female")
# print ("Средняя оценка за экзамен у женщин: %.2f" %exam_female)

# б) наличие опыта
# Функция расчета средней оценки за домашние задания в зависимости от наличия опыта:
def get_home_average_exp(exp):
  average = 0                                          
  quantity = 0 
  for student in students:
    if student["experience"] == exp:
      average += sum(student["homework"])/len(student["homework"])
      quantity += 1 
  home_average_exp = average/quantity
  return home_average_exp
# Функция вывода на экран средней оценки за домашние задания у студентов с опытом:
average_exp = get_home_average_exp(1)
# print ("Средняя оценка за домашние задания у студентов с опытом: %.2f" %average_exp)
# Функция вывода на экран средней оценки за домашние задания у студентов без опыта:
average_out_exp = get_home_average_exp(0)
# print ("Средняя оценка за домашние задания у студентов без опыта: %.2f" %average_out_exp)

# Функция расчета средней оценки за экзамен в зависимости от наличия опыта:
def get_exam_average_exp(exp):
  average_exam = 0                                          
  quantity = 0 
  for student in students:
    if student["experience"] == exp:
      average_exam += student["exam"]
      quantity += 1 
  average_exam /= quantity
  return average_exam
# Функция вывода на экран средней оценки за экзамен у студентов с опытом:
exam_exp = get_exam_average_exp(1)
# print ("Средняя оценка за экзамен у студентов с опытом: %.2f" %exam_exp)
# Функция вывода на экран средней оценки за экзамен без опыта:
exam_out_exp = get_exam_average_exp(0)
# print ("Средняя оценка за экзамен у студентов без опыта: %.2f" %exam_out_exp)

# Опреледим лучшего студента, у которого будет максимальный балл по формуле 0.6 * его средняя оценка за домашние задания + 0.4 * оценка за экзамен в виде:
# Лучший студент: S с интегральной оценкой Z
# если студент один или:
# Лучшие студенты: S... с интегральной оценкой Z
# если студентов несколько, где S - имя/имена студентов, Z - вычисляемое значение.

def the_best_student():
  best_score = 0    # лучшая оценка
  for student in students:
    average_home = sum(student["homework"])/len(student["homework"])
    score_exam = student["exam"]
    max_score = 0.6*average_home + 0.4*score_exam
    if max_score > best_score:
      best_score = max_score
      best_student = student["name"] + ' ' + student["surname"]
  return best_student, best_score

student_best, score_best = the_best_student()

# Функция поиска лучших студентов:
def the_best_students():
  best_score = 0 # текущее значение интегральной оценки
  best_score_list = [] # создадим пустой список лучших оценок
  best_students_list = [] # пустой список лучших студентов
  for student in students:
    new_dict = {} # создадим новый словарь
    best_score = sum(student["homework"])/len(student["homework"]) * 0.6 + (student["exam"] * 0.4) # расчет интегральной оценки студента по формуле
    name_surname_key = student["name"] + " " + student["surname"] # введем переменную = ключу словаря из списка ("name"+"surname")
    new_dict[name_surname_key] = best_score # зададим, что ключ словаря ("name" + "surname") = интегральной оценки
    best_score_list.append(best_score) # список с интегральными оценками студентов

# Найдем список лучших оценок:    
    max_score = max(best_score_list) # получим max оценку среди студентов
    if best_score == max_score: # если интегр.оценка = max, то добавим в список лучших студентов
      best_students_list.append(new_dict)  

# Находим список лучших студентов с максимальной оценкой  
  name_surname_list = []
  for student in best_students_list:
    for key, values in student.items():
      if values == max_score:
        name_surname_list.append(key)

# добавим переменную, которая будет выводить именя лучших студентов в списке через запятую:
  more_than_one =  ", ".join(name_surname_list)
# Напишем условие вывода на экран списка лучших студентов или лучшего студента:  
  if len(name_surname_list) == 1:
    print("Лучший студент: {} c интегральной оценкой {} баллов".format(name_surname_list, best_score))
  else: 
    print("Лучшие студенты: {} c интегральной оценкой {} баллов".format(more_than_one, best_score))
  
  # for student in best_students_list:
  #   for key, values in student.items():
  #     if values == max_score and len(name_surname_list) >= 1:
  #       print("Лучшие студенты: {} с интегральной оценкой {:.2f}".format(more_than_one, values))
  #     elif values == max_score and len(name_surname_list) == 1:
  #       print("Лучший студент: {} с интегральной оценкой {:.2f}".format(key, values))
 
# the_best_students()

# Вывод пользовательских программ на экран:          
def main():
  print("Выберите одну из команд: \n"
  "1 - Узнать среднюю оценку за домашние задания и за экзамен по всем группе; \n"
  "2 - Вывести среднеюю оценку за домашние задания и за экзамен по группе в разрезе: а)пола б)наличия опыта; \n"
  "3 - Узнать лучшего студента; \n")

  user_input = input("Введите вариант ответа (1, 2, 3): ")
  if user_input == "1":
    print ("Средняя оценка за домашние задания по группе: %.2f" %average_home_group)
    print("Средняя оценка за экзамен по группе: %.2f" %average_exam_group)
  elif user_input == "2":
    print ("a)")
    print ("Средняя оценка за домашние задания у мужчин: %.2f" %average_male)
    print ("Средняя оценка за экзамен у мужчин: %.2f" %exam_male)
    print ("Средняя оценка за домашние задания у женщин: %.2f" %average_female)
    print ("Средняя оценка за экзамен у женщин: %.2f" %exam_female)
    print("б)")
    print ("Средняя оценка за домашние задания у студентов с опытом: %.2f" %average_exp)
    print ("Средняя оценка за экзамен у студентов с опытом: %.2f" %exam_exp)
    print ("Средняя оценка за домашние задания у студентов без опыта: %.2f" %average_out_exp)
    print ("Средняя оценка за экзамен у студентов без опыта: %.2f" %exam_out_exp)
  elif user_input == "3":
    print(the_best_students())
   else:
    print('Введено недопустимое значение, попробуйте ещё раз.')

main()

