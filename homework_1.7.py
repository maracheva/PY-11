# Необходимо реализовать классы животных на ферме:

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:

# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.

# Создадим общий класс
class Fauna():
    name = ['animal', 'bird']
    size = ['big', 'small']
    paws = [2, 4]
    wings = ['Yes', 'None']

    def __init__(self, name, size, paws, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.wings = wings
        print (self.name, self.size, self.paws, self.wings)

        def info(self):
            print(self.name, self.size, self.paws, self.wings)

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'wings': self.wings,
        })


class Birds(Fauna):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Fauna.__init__(self, name_bird, 'small', 2, 'Yes')


class Animal(Fauna):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']
    def __init__(self, name_animal):
        self.name_animal = name_animal
        Fauna.__init__(self, name_animal, 'big', 4, 'None')


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')

Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

# print(Birds._dict_)
print('\n Класс Птицы:',
      '\n Утки: {}' .format(ducks),
      '\n Куры: {}' .format(chickens),
      '\n Гуси: {}' .format(geese))

print('\n Класс Животные:',
      '\n Коровы: {}'.format(Cows),
      '\n Козы: {}'.format(Goats),
      '\n Овцы: {}'.format(Sheep),
      '\n Свиньи: {}'.format(Pigs))
