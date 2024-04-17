

## Задача 1

# notion


import statistics as s

print(s.mean([1, 2, 3, 4, 5]))


## Задача 2

#notion


## Задача 3

import sys

sys.setrecursionlimit(2000)


def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)


print(recursive_function(1000, 0))



## Задача 4

import re

text = 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'
nums = re.findall('\d+', text)

print(nums)


## Задача 5


from random import randint as rnd, choice as chc

array = []
for n in range(1, 11):
    array.append(rnd(1, 100))

print('Список случайных чисел:', array)
print('Случайное число из списка:', chc(array))


## Задача 6

from math import *


def quad_equat(a, b, c):
    disc = b * b - 4 * a * c
    sqrt_val = sqrt(abs(disc))

    if disc > 0:
        x1 = (-b + sqrt_val) / (2 * a)
        x2 = (-b - sqrt_val) / (2 * a)
        if (x1 > x2):
            print(f'Квадратное уравнение имеет два корня: {x1} и {x2}')
        else:
            print(f'Квадратное уравнение имеет два корня: {x2} и {x1}')

    elif disc == 0:
        x1 = -b / (2 * a)
        print(f'Квадратное уравнение имеет один корень: {x1}')

    else:
        print('Нет корней')


a = int(input('Введите значение переменной a: '))
b = int(input('Введите значение переменной b: '))
c = int(input('Введите значение переменной c: '))

if a == 0:
    print('Введите корректное значение переменной a')
else:
    quad_equat(a, b, c)

## Задача 7


from datetime import datetime

print(datetime.now().time())


## Задача 8

#notion

## Задача 9


from sys import version_info


def py_version():
    print(f'Python {version_info.major}.{version_info.minor}.{version_info.micro}')


py_version()


## Задача 10


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Деление на ноль!')
    return a / b


from calculator import *

while True:
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Умножение')
    print('4. Деление')
    print('5. Выход')
    op = int(input('Выберите математическую операцию: '))
    if op == 5:
        print('Пока-пока!')
        break

    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))

    if op == 1:
        print(f'Результат сложения: {add(a, b)} \n')
    if op == 2:
        print(f'Результат вычитания: {subtract(a, b)} \n')
    if op == 3:
        print(f'Результат умножения: {multiply(a, b)} \n')
    if op == 4:
        print(f'Результат деления: {divide(a, b)} \n')


## Задача 11


from importlib import import_module


def imp_mods(mods):
    glb = globals()
    if mods:
        for m in mods:
            glb[m] = import_module(m)
            print(f'Модуль {m} успешно импортирован!')


imp_mods(['random', 'math'])
print(math.factorial(random.randint(1, 10)))


## Задача 12


from math import *


def square(side_d=15):
    print(f'Периметр квадрата: {(side_d * 4)}')
    print(f'Площадь квадрата: {pow(side_d, 2)}')


def circle(radius=5):
    print(f'Длина окружности: {pi * pow(radius, 2)}')
    print(f'Площадь окружности: {pi * 2 * radius}')


def triangle(side_a=7, side_b=2, side_c=8):
    print(f'Периметр треугольника: {side_a + side_b + side_c}')
    p = (side_a + side_b + side_c) / 2
    print(f'Площадь треугольника: {sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))}')



