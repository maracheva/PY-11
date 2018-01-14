# pip


class Pets: # родительский класс Pets - домашние животные
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
    # def __init__(self, name, type, family, wings, paws):
    #     super().__init__(name, type, family, wings, paws)
    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        self.feathers = feathers
        print('{} даёт в среднем {} гр пуха и пера.'.format(self.name, self.feathers))


class Geese(Birds):  # Класс Гуси
    # def __init__(self, name, type, family, wings, paws):
    #     super().__init__(name, type, family, wings, paws)
    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        self.feathers = feathers
        print('{} даёт в среднем {} гр пуха и пера.'.format(self.name, self.feathers))


class Chickens(Birds):  # Класс Курицы
    # def __init__(self, name, type, family, wings, paws):
    #     super().__init__(name, type, family, wings, paws)

    def __str__(self):
        return str('Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во крыльев: {}; \nТип лапок: {}.'.format(self.group,
                                                                                                          self.type,
                                                                                                          self.family,
                                                                                                          self.wings,
                                                                                                          self.paws))

    def give_feathers(self, feathers):  # дают пух и перо
        self.feathers = feathers
        print('{} даёт в среднем {} гр пуха и пера.'.format(self.name, self.feathers))

    def give_eggs_to_day(self, eggs):
        self.eggs = eggs
        print('Количество яиц в день (от несушки): {} шт.'.format(self.eggs))


class Animal(Pets):  # Класс Животные
    def __init__(self, name, group, type, family, horns, hoofs):
        self.hoofs = hoofs
        self.horns = horns
        super().__init__(name, group, type, family)


class Cows(Animal):  # Класс Корова
    # def __init__(self, name, type, family, horns, hoofs):
    #     super().__init__(name, type, family, horns, hoofs)
    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nТип копыт: {}.'.format(self.group, self.type,
                                                                                                 self.family,
                                                                                                 self.horns,
                                                                                                 self.hoofs))

    def give_milk(self, milk):
        self.milk = milk
        print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))


class Goats(Animal):  # Класс Козы
    # def __init__(self, name, type, family, horns, hoofs):
    #     super().__init__(name, type, family, horns, hoofs)

    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nТип копыт: {}.'.format(self.group, self.type,
                                                                                                 self.family,
                                                                                                 self.horns,
                                                                                                 self.hoofs))

    def give_milk(self, milk):
        self.milk = milk
        print('{} даёт в среднем {} литров молока в месяц.'.format(self.name, self.milk))

    def give_wool(self, wool):
        self.wool = wool
        print('{} дает примерно {} гр шерсти в год.'.format(self.name, self.wool))


class Sheep(Animal):  # Класс Овцы
    # def __init__(self, name, type, family, horns, hoofs):
    #     super().__init__(name, type, family, horns, hoofs)

    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nТип копыт: {}.'.format(self.group, self.type,
                                                                                                 self.family,
                                                                                                 self.horns,
                                                                                                 self.hoofs))

    def give_wool(self, wool):
        self.wool = wool
        print('{} дает примерно {} кг шерсти в год.'.format(self.name, self.wool))


class Pigs(Animal):  # Класс Свиньи
    # def __init__(self, name, type, family, horns, hoofs):
    #     super().__init__(name, type, family, horns, hoofs)

    def __str__(self):
        return str(
            'Класс: {}; \nТип: {}; \nСемейство: {}; \nКол-во рогов: {}; \nТип копыт: {}.'.format(self.group, self.type,
                                                                                                 self.family,
                                                                                                 self.horns,
                                                                                                 self.hoofs))


bird_1 = Ducks('Утка', 'Птицы', 'Водоплавающие', 'Утинных', 2, 'перепончатые')
bird_1.info()
print(bird_1)
bird_1.give_feathers('50-60')

print()
bird_2 = Geese('Гусь', 'Птицы', 'Водоплавающие', 'Утинных гусеобразных', 2, 'перепончатые')
bird_2.info()
print(bird_2)
bird_2.give_feathers('250-280')

print()
bird_3 = Chickens('Курица', 'Птицы', 'Неводоплавающие', 'Фазановых', 2, 'Без перепонок')
bird_3.info()
print(bird_3)
bird_3.give_feathers('130-200')
bird_3.give_eggs_to_day('1-2')

print()
animal_1 = Cows('Корова', 'Млекопитающие', 'Жвачных парнокопытных', 'Полорогих', 2, 4)
animal_1.info()
print(animal_1)
animal_1.give_milk(300)

print()  # пустая строка для разделения абзацев
animal_2 = Goats('Коза', 'Млекопитающие', 'Жвачные парнокопытные', 'Полорогие', 2, 4)
animal_2.info()
print(animal_2)
animal_2.give_milk(100)
animal_2.give_wool(250)

print()  # пустая строка для разделения абзацев
animal_3 = Sheep('Овца', 'Млекопитающие', 'Жвачные парнокопытные', 'Полорогие', 2, 4)
animal_3.info()
print(animal_3)
animal_3.give_wool('2-3')

print()  # пустая строка для разделения абзацев
animal_4 = Pigs('Свинья', 'Млекопитающие', 'Нежвачные парнокопытные', 'Всеядные', 0, 4)
animal_4.info()
print(animal_4)
