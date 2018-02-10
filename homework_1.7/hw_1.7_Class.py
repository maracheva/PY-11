#coding: utf-8


class Pets:  # родительский класс Pets - домашние животные
    def __init__(self, name, group, type, family):
        self.name = name
        self.kind = "домашнее животное"
        self.group = group
        self.type = type
        self.family = family

    def info(self):
        print("{} - это {}.".format(self.name, self.kind))


class Birds(Pets):  # Класс "Птицы"
    def __init__(self, name, group, type, family, wings, paws):
        self.wings = wings
        self.paws = paws
        super().__init__(name, group, type, family)


class Ducks(Birds):  # Класс Утки
    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        feathers_norm = 50  # грамм в среднем с одной птицы
        self.feathers = feathers
        print('Эта {} даёт в среднем {} гр пуха и пера.'.format(self.name.lower(), self.feathers))
        if self.feathers < feathers_norm:
            print('Пуха и пера недостаточно.')


class Geese(Birds):  # Класс Гуси
    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        feathers_norm = 250  # грамм в среднем с одной птицы
        self.feathers = feathers
        print('Этот {} даёт в среднем {} гр пуха и пера.'.format(self.name.lower(), self.feathers))
        if self.feathers < feathers_norm:
            print('Пуха и пера недостаточно.')


class Chickens(Birds):  # Класс Курицы
    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        feathers_norm = 150  # грамм в среднем с одной птицы
        self.feathers = feathers
        print('Эта {} даёт в среднем {} гр пуха и пера.'.format(self.name.lower(), self.feathers))
        if self.feathers < feathers_norm:
            print('Пуха и пера недостаточно.')

    def give_eggs_to_day(self, eggs):
        self.eggs = eggs
        if self.eggs >= 1:
            print(f'Это курица - несушка, она дает {self.eggs} яйца в день')
        else:
            print(f'Это обычная курица, она дает {self.eggs} яиц в день ')


class Animal(Pets):  # Класс Животные
    def __init__(self, name, group, type, family, horns, hoofs):
        self.hoofs = hoofs
        self.horns = horns
        super().__init__(name, group, type, family)


class Cows(Animal):  # Класс Корова
    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.'.format(self.group,
                                                                                                    self.type,
                                                                                                    self.family,
                                                                                                    self.horns,
                                                                                                    self.hoofs))

    def give_milk(self, milk):
        self.milk = milk
        if self.milk > 0:
            print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))
        else:
            print('Это животное не дает молока')


class Goats(Animal):  # Класс Козы
    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.'.format(self.group,
                                                                                                    self.type,
                                                                                                    self.family,
                                                                                                    self.horns,
                                                                                                    self.hoofs))

    def give_milk(self, milk):
        self.milk = milk
        while True:
            if self.milk:
                print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))
                break
            else:
                print('Это животное не дает молока')
                break

    def give_wool(self, wool):
        self.wool = wool
        print('{} дает примерно {} гр шерсти в год.'.format(self.name, self.wool))


class Sheep(Animal):  # Класс Овцы
    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.'.format(self.group,
                                                                                                    self.type,
                                                                                                    self.family,
                                                                                                    self.horns,
                                                                                                    self.hoofs))

    def give_milk(self, milk):
        self.milk = False
        while True:
            if self.milk:
                print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))
                break
            else:
                print('Это животное не дает молока')
                break


class Pigs(Animal):  # Класс Свиньи
    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nКол-во копыт: {}.'.format(self.group,
                                                                                                    self.type,
                                                                                                    self.family,
                                                                                                    self.horns,
                                                                                                    self.hoofs))

    def give_milk(self, milk):
        self.milk = False
        while True:
            if self.milk:
                print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))
                break
            else:
                print('Это животное не дает молока')
                break


bird_1 = Ducks('Утка', 'Птицы', 'Водоплавающие', 'Утинных', 2, 'перепончатые')
print(bird_1)
bird_1.give_feathers(40)

print()
bird_2 = Geese('Гусь', 'Птицы', 'Водоплавающие', 'Утинных гусеобразных', 2, 'перепончатые')
print(bird_2)
bird_2.give_feathers(250)

print()
bird_3 = Chickens('Курица', 'Птицы', 'Неводоплавающие', 'Фазановых', 2, 'Без перепонок')
print(bird_3)
bird_3.give_feathers(130)
bird_3.give_eggs_to_day(2)

print()
animal_1 = Cows('Корова', 'Млекопитающие', 'Жвачных парнокопытных', 'Полорогих', 2, 4)
print(animal_1)
animal_1.give_milk(300)

print()  # пустая строка для разделения абзацев
animal_2 = Goats('Коза', 'Млекопитающие', 'Жвачные парнокопытные', 'Полорогие', 2, 4)
print(animal_2)
animal_2.give_milk(100)

print()  # пустая строка для разделения абзацев
animal_3 = Sheep('Овца', 'Млекопитающие', 'Жвачные парнокопытные', 'Полорогие', 2, 4)
print(animal_3)
animal_3.give_milk(False)

print()  # пустая строка для разделения абзацев
animal_4 = Pigs('Свинья', 'Млекопитающие', 'Нежвачные парнокопытные', 'Всеядные', 0, 4)
print(animal_4)
animal_4.give_milk(False)

