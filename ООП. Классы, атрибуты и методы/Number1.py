class CoffeMachine:
    ''' Этот класс является моделью кофемашины. Её можно пополнить с помощью методов класса, это будет делать пользователь. Если пользователь внёс'
    недостаточное количество компонентов (содержимое в них для определенного вида кофе), то программа выдаст ошибку. Излишки'
    компонентов после сделанного кофе утилизируются, ведь мы можем только одно кофе приготовить за раз, загрузив в кофемашину ресурсы для него.'
    Будем считать, что это нужно для того, чтобы машина самоочистилась после одной кружки, чтобы следующую было готовить в чистой машине :)
    Я изменил условие задачи немного в логичную сторону - я для каждого типа кофе проверяю определенные ресурсы, чтобы определить,
    можно ли сделать такой тип кофе. Для каждого типа разное количество требуется значений в параметрах. '''

    def __init__(self, type, water_level=0, coffe_level=0, milk_level=0, sugar_level=0, caps=0):
        self.water_level = water_level
        self.coffe_level = coffe_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.caps = caps
        self.type = type

    def add_water(self, amount):
        self.water_level += amount

    def add_coffe(self, amount):
        self.coffe_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_caps(self, number):
        self.caps += number

    def check_resources(self):
        if self.type == 'Latte':
            if self.water_level >= 100 and self.coffe_level >= 25 and self.milk_level >= 100 and self.sugar_level >= 5 and self.caps >= 1:
                return True
            else:
                return False
        elif self.type == 'Expresso':
            if self.water_level >= 75 and self.coffe_level >= 20 and self.milk_level >= 125 and self.sugar_level >= 2 and self.caps >= 1:
                return True
            else:
                return False
        elif self.type == 'Capuccino':
            if self.water_level >= 125 and self.coffe_level >= 20 and self.milk_level >= 75 and self.sugar_level >= 3 and self.caps >= 1:
                return True
            else:
                return False

    def make_coffe(self):
        if self.type == 'Latte':
            bul = self.check_resources()
            if bul:
                water_level = self.water_level
                water_level -= 100
                coffe_level = self.coffe_level
                coffe_level -= 25
                milk_level = self.milk_level
                milk_level -= 100
                sugar_level = self.sugar_level
                sugar_level -= 5
                caps = self.caps
                caps -= 1
                return f'Ваше {self.type} готово к потреблению!'
            else:
                return f'Ваше {self.type} не было сделано, ведь не хватило количества компонентов для приготовления кофе'
        if self.type == 'Expresso':
            bul = self.check_resources()
            if bul:
                water_level = self.water_level
                water_level -= 75
                coffe_level = self.coffe_level
                coffe_level -= 20
                milk_level = self.milk_level
                milk_level -= 125
                sugar_level = self.sugar_level
                sugar_level -= 2
                caps = self.caps
                caps -= 1
                return f'Ваше {self.type} готово к потреблению!'
            else:
                return f'Ваше {self.type} не было сделано, ведь не хватило количества компонентов для приготовления кофе'
        if self.type == 'Capuccino':
            bul = self.check_resources()
            if bul:
                water_level = self.water_level
                water_level -= 125
                coffe_level = self.coffe_level
                coffe_level -= 20
                milk_level = self.milk_level
                milk_level -= 75
                sugar_level = self.sugar_level
                sugar_level -= 3
                caps = self.caps
                caps -= 1
                return f'Ваше {self.type} готово к потреблению!'
            else:
                return f'Ваше {self.type} не было сделано, ведь не хватило количества компонентов для приготовления кофе'


print(CoffeMachine.__doc__)
print('Выберите тип вашего кофе')
type_coffe = input()
print(
    'Учтите, что для каждого вида кофе свои компоненты, которые имеют разные значения, если вы внесете меньше, чем нужно для приготовления кофе, то оно не сделается')
CoffeMachine_1 = CoffeMachine(type_coffe)
print(f'Залейте в автомат нужное количество воды для {type_coffe}')
CoffeMachine_1.add_water(int(input()))
print(f'Положите в автомат нужное количество кофе для {type_coffe}')
CoffeMachine_1.add_coffe(int(input()))
print(f'Залейте в автомат нужное количество молока для {type_coffe}')
CoffeMachine_1.add_milk(int(input()))
print(f'Добавьте в автомат нужное количество сахара для {type_coffe}')
CoffeMachine_1.add_sugar(int(input()))
print(f'Выберите, сколько кружек {type_coffe} вы хотите, а затем - поставьте их в автомат')
CoffeMachine_1.add_caps(int(input()))
print(CoffeMachine_1.make_coffe())
