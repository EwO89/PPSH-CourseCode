

## Задача 1


from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class Autobiography(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в автобиографическом жанре. Автор - {self.author}')


class Psychology(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в жанре психологии. Автор - {self.author}')


class Fantasy(Book):
    def display(self):
        print(f'"{self.title}" - прекрасная книга, написанная в жанре фэнтези. Автор - {self.author}')




## Задача 2

#дал ответ в notion

## Задача 3




class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        print('Очень интересный вопрос! Давай разбираться вместе.')


class Student(Human):

    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        print()


class Teacher(Human):

    def answer_question(self, question):
        if question == 'как научится программировать?':
            print('Сейчас расскажу')
        elif question == 'как войти в айти?':
            print('Можешь начать осваивать программирование с ППШ')
        else:
            super().answer_question(question)


class Mentor(Human):

    def answer_question(self, question):
        if question == 'как повысить эффективность работы?':
            print('Важно соблюдать три правила')
        elif question == 'зачем быть альтруистом в 2023?':
            print('У меня есть ответ на твой вопрос')
        else:
            super().answer_question(question)


class Curator(Human):

    def answer_question(self, question):
        if question == 'как додуматься до этого решения?':
            print('Сейчас опишу ход мыслей при решении задачи')
        else:
            super().answer_question(question)


class CodeReviewer(Human):

    def answer_question(self, question):
        if question == 'я усовершенствовал свой код. Вы проверите?':
            print('Проверил. Замечательный вариант решения. Вы отлично справились!')
        else:
            super().answer_question(question)




## Задача 4




class GeometricFigures:

    def get_perimeter(self):
        raise NotImplementedError('Переопределите метод get_perimeter в дочернем классе')


class Triangle(GeometricFigures):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c}.'

    def get_perimeter(self):
        return f'Периметр равен: {self.a + self.b + self.c}'


class Square(GeometricFigures):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Квадрат со стороной {self.side}.'

    def get_perimeter(self):
        return f'Периметр равен: {4 * self.side}'


class Rectangle(GeometricFigures):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a}, {self.b}.'

    def get_perimeter(self):
        return f'Периметр равен: {2 * (self.a + self.b)}'




## Задача 5


from abc import ABC, abstractmethod


class Lock(ABC):
    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class Command(ABC):
    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class SmartAssistant(Command):

    def close_lock(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def open_lock(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def vote_command(self):
        print('Умный помощник распознал голосовую команду')

    def gesture_command(self):
        print('Умный помощник распознал жестовые команды')


class SmartCamera(Lock, Command):

    def close_lock(self):
        print('Умная камера закрыла замок входной двери')

    def open_lock(self):
        print('Умная камера открыла замок входной двери')

    def vote_command(self):
        print('Умная камера распознала голосовую команду')

    def gesture_command(self):
        print('Умная камера распознала жестовые команды')


class SmartLock(Lock):

    def close_lock(self):
        print('Умный замок закрыл входную дверь')

    def open_lock(self):
        print('Умный замок открыл входную дверь')

    def vote_command(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')

    def gesture_command(self):
        raise NotImplementedError('Умный помощник не может выполнить данную команду')


