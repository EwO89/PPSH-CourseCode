# Модули

## Задача 1

Импортируйте из модуля `statistics` стандартной библиотеки функцию `mean()`, которая возвращает приблизительное среднее арифметическое элементов последовательности. Используйте различные способы: 

1) через импорт библиотеки;
2) через импорт всех объектов;
3) через импорт конкретной функции;
4) с помощью импорта функции с переименованием;
5) с помощью импорта модуля с переименованием.

Используя необходимые атрибуты модуля, выведите на экран результат работы функции `mean()`.

## Задача 2

Выведите полный список всех модулей, установленных в исполняемую среду. Для этого используйте различные способы: 

1) через функцию `help()`;

    Программа должна вывести все модули и пакеты (как встроенные, установленные, так и созданные нами), доступные для главного скрипта.

2) через модуль `sys`;

    Программа должны вывести только встроенные или загруженные библиотеки.

3) через функцию `dir()`;

    Программа должна вывести модули, используемые в конкретной программе, а также созданные константы и отдельные объекты импортированных библиотек.

4) с помощью консоли;

    Предоставляется доступ ко всем установленным модулям и пакетам (внутри окружения) и их версиям.

## Задача 3

Представленная ниже программа не работает, возникает ошибка RecursionError: maximum recursion depth exceeded in comparison (максимальная глубина рекурсии превышена). Модуль `sys` предоставляет доступ к функции `setrecursionlimit()` для изменения предела рекурсии. Подключите модуль `sys`, в качестве ответа укажите выведенное число.

```py
def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)
    
print(recursive_function(1000, 0))
```

## Задача 4

Извлеките все цифры из данного фрагмента текста: 'ул. Кутузовская, дом № 13, корпус 3, квартира 98'. Для решения данного задания импортируйте из модуля `re` стандартной библиотеки функцию `findall()`. Далее используйте цепочку `re.findall('\d+', text)`.

## Задача 5

Импортируйте из модуля `random` стандартной библиотеки функции `randint()` и `choice()`, использовав для них псевдонимы `rnd` и `chc`. Создайте список array и заполните его десятью случайными целыми числами от 1 до 100. Выведите на экран сам список, а также случайный элемент списка.

## Задача 6

На вход программе подается три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения $$ax^{2}+bx+c=0$$ Рассмотрите все возможные варианты значений коэффициентов уравнения. Для решения данного задания импортируйте из модуля `math` стандартной библиотеки необходимые функции.

## Задача 7

Выведите на экран текущее время. Для решения задачи импортируйте из модуля `datetime` стандартной библиотеки класс `datetime`. Далее используйте цепочку `datetime.now().time()`, которая как раз и вернет текущее время.

## Задача 8

Не запуская код, попробуйте догадаться: что выведет данная программа? В ответе укажите два значения без разделителей.

```py
    from datetime import date, timedelta
    d1 = date.fromisoformat('2023-06-09')
    d2 = date(2023, 5, 31)
    if (d1 > d2):
        delta = d1 - d2
        print(delta.days)
        delta2 = timedelta(days=30)
        print((d1 + delta2).weekday()+1)
```
## Задача 9

Создайте собственный модуль `py_version`, который выводит на экран текущую версию интерпретатора в формате "Python major.minor.micro". Для выполнения данного задания импортируйте в собственный модуль локальную область видимости функции `version_info` модуля `sys` стандартной библиотеки. Выведите на экран результат работы собственного модуля `py_version`.

## Задача 10

Создайте собственный модуль `calculator`, содержащий функции, определяющие математические операции: `add()` (сложение), `subtract()` (вычитание), `multiply()` (умножение), `divide()` (деление). В основной программе создайте консольную программу калькулятор, для вычисления выражений воспользуйтесь функциями из модуля.

## Задача 11

Создайте собственный модуль `imp_modules`, импортирующий в глобальную область видимости текущего модуля необходимые пакеты и модули. Ваш модуль должен содержать функцию `imp_modules(mods)`, которая принимает кортеж или список имен пакетов и модулей для импорта. Импортируйте при помощи созданной функции модули `random` и `math`, а затем выведите на экран факториал случайного положительного целого числа не превышающего десяти.

## Задание 12

Создайте собственный модуль для вычисления параметров геометрических фигур. Модуль geometry.py должен содержать следующие функции: 

- Функция `circle()` принимает на вход только один параметр -- радиус, возвращает значения площади окружности и длины окружности. Функция `circle()` содержит дефолтный радиус (r = 5), на случай если пользователь не введет.
- Функция `triangle()` принимает на вход три параметра -- стороны треугольника, возвращает значения периметра и площади треугольника. Если пользователь не вводит параметры, то функция `triangle()` использует значения сторон по умолчанию (a = 7, b = 2, c = 8). Помимо этого функция осуществлять проверку существования треугольника по введенным сторонам. 
- Функция `square()` принимает на вход один параметр -- сторону квадрата, возвращает периметр и площадь квадрата. Дополнительная переменная (a = 15) используется функцией `square()`, если пользователь не предоставил параметры фигуры.
