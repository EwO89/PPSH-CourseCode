
## Задача 1


import matplotlib.pyplot as plt

# Заданные данные о температурах
temperatures = [25, 28, 30, 27, 22, 24, 26]
days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

# Создание графика
plt.plot(days_of_week, temperatures)

# Настройка осей и заголовка графика
plt.xlabel('Дни недели')
plt.ylabel('Температура (градусы)')
plt.title('Ежедневные температуры в городе за неделю')

# Отображение графика
plt.show()




## Задача 2


import matplotlib.pyplot as plt

# Результаты опроса
music_genres = ['Рок', 'Поп', 'Хип-хоп', 'Электронная', 'Классическая']
votes = [30, 20, 15, 10, 25]

# Создание круговой диаграммы
plt.pie(votes, labels=music_genres, autopct='%1.1f%%')

# Добавление заголовка диаграммы
plt.title('Предпочтения музыкальных жанров')

# Показать диаграмму
plt.show()




## Задача 3


import matplotlib.pyplot as plt

# Результаты матчей
matches = ['Матч 1', 'Матч 2', 'Матч 3', 'Матч 4', 'Матч 5']
goals_scored = [2, 3, 1, 4, 2]
goals_conceded = [1, 2, 0, 3, 1]

# Создание столбчатой диаграммы
plt.bar(matches, goals_scored, label='Забитые голы')
plt.bar(matches, goals_conceded, label='Пропущенные голы')

# Добавление легенды
plt.legend()

# Добавление подписей осей и заголовка диаграммы
plt.xlabel('Матчи')
plt.ylabel('Голы')
plt.title('Результаты матчей')

# Показать диаграмму
plt.show()




## Задача 4


import matplotlib.pyplot as plt

# Данные о продажах фруктов
fruits = ['Яблоки', 'Груши', 'Бананы', 'Апельсины', 'Персики']
sales = [100, 85, 70, 60, 45]

# Создание горизонтальной столбчатой диаграммы
plt.barh(fruits, sales)

# Добавление подписей осей и заголовка диаграммы
plt.xlabel('Количество продаж')
plt.ylabel('Фрукты')
plt.title('Продажи фруктов')

# Показать диаграмму
plt.show()




## Задача 5


import matplotlib.pyplot as plt

# Создаем список значений x от 1 до 49
x = range(1, 50)

# Создаем список значений y, умножая каждое значение x на 3
y = [value * 3 for value in x]

# Строим линию на графике
plt.plot(x, y)

# Устанавливаем название оси x
plt.xlabel('Ось x')

# Устанавливаем название оси y
plt.ylabel('Ось y')

# Устанавливаем заголовок графика
plt.title('Нарисуй линию')

# Отображаем график
plt.show()


## Задача 6


import matplotlib.pyplot as plt

# Создаем списки значений для первой линии
x1 = [10, 20, 30]
y1 = [20, 40, 10]

# Создаем списки значений для второй линии
x2 = [10, 20, 30]
y2 = [40, 10, 30]

# Строим первую линию
plt.plot(x1, y1, label="Линия 1")

# Строим вторую линию
plt.plot(x2, y2, label="Линия 2")

# Устанавливаем название оси x
plt.xlabel('Ось x')

# Устанавливаем название оси y
plt.ylabel('Ось y')

# Устанавливаем заголовок графика
plt.title('Нарисуй график')

# Добавляем легенду
plt.legend()

# Отображаем график
plt.show()



## Задача 7


import matplotlib.pyplot as plt

# Данные о посещениях сайта A
site_a = [50, 60, 70, 80, 90]

# Данные о посещениях сайта B
site_b = [40, 55, 75, 85, 95]

# Создаем рисунок и оси с помощью функции subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Настраиваем оси для первого графика (посещения сайта A)
axs[0].set_title('Посещения сайта A')
axs[0].set_xlabel('День')
axs[0].set_ylabel('Количество посещений')
axs[0].plot(site_a)

# Настраиваем оси для второго графика (посещения сайта B)
axs[1].set_title('Посещения сайта B')
axs[1].set_xlabel('День')
axs[1].set_ylabel('Количество посещений')
axs[1].plot(site_b)

# Отображаем рисунок
plt.show()


## Задача 8


import matplotlib.pyplot as plt

# Список языков программирования
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']

# Список популярности каждого языка программирования
popularity = [22, 18, 9, 8, 7, 6]

# Создаем список позиций для каждого языка программирования
x_pos = [i for i, _ in enumerate(x)]

# Создаем столбчатую диаграмму с указанием цветов для каждого столбца
plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

# Задаем подписи для осей и заголовок диаграммы
plt.xlabel("Языки программирования")
plt.ylabel("Популярность")
plt.title("Популярность языков программирования")

# Устанавливаем значения для оси X
plt.xticks(x_pos, x)

# Включаем вспомогательные деления на осях
plt.minorticks_on()

# Включаем сетку для основных делений
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

# Включаем сетку для вспомогательных делений
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Отображаем диаграмму
plt.show()




## Задача 9


import matplotlib.pyplot as plt

# Создание объекта фигуры
fig = plt.figure()

# Список шаблонов для заливки
patterns = ["|", "\\", "/", "+", "-", ".", "*", "x", "o", "O"]

# Добавление подграфика к фигуре
ax = fig.add_subplot(111)

# Итерация по шаблонам и добавление столбца на график с заданными параметрами
for i in range(len(patterns)):
    ax.bar(i, 3, color='white', edgecolor='black', hatch=patterns[i])

# Отображение графика
plt.show()


## Задача 10


import matplotlib.pyplot as plt
import random

# Устанавливаем начальное состояния генератора случайных чисел
random.seed(0)

# Генерируем 200 случайных значений X с нормальным распределением
X = [random.gauss(0, 1) for _ in range(200)]

# Генерируем 200 случайных значений Y с нормальным распределением
Y = [random.gauss(0, 1) for _ in range(200)]

# Создаем точечную диаграмму со случайными значениями X и Y
plt.scatter(X, Y, color='r')

# Добавляем подпись для оси X
plt.xlabel("X")

# Добавляем подпись для оси Y
plt.ylabel("Y")

# Отображаем график
plt.show()

