
## Задача 1


from random import *


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()

        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        if self.__is_number(number):
            if number in self.__abiturients:
                raise ValueError("Абитуриент уже внесён в базу")
            self.__abiturients[number] = abiturient
        else:
            raise ValueError("СНИЛС введён некорректно")

    def get_status(self, number):
        return self.__abiturients[number].get_status()

    # проверка на корректность СНИЛСа
    @staticmethod
    def __is_number(number):
        return number[0:3].isdigit() and number[3] == "-" and number[4:7].isdigit() and \
            number[7] == "-" and number[8:11].isdigit() and number[11] == " " and number[12:].isdigit()


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # СНИЛС
        self.__number = number

        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()

        # есть ли БВИ
        self.__bvi = bvi

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__check_name(name)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = self.__check_name(surname)

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        self.__patronymic = self.__check_name(patronymic)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            raise ValueError

    @property
    def bvi(self):
        return self.__bvi

    @bvi.setter
    def bvi(self, bvi):
        if isinstance(bvi, bool):
            self.__bvi = bvi
        else:
            raise ValueError

    @property
    def RNE(self):
        return self.__RNE

    # проверка, все ли результаты ЕГЭ корректны
    @RNE.setter
    def RNE(self, RNE):
        if isinstance(RNE, tuple):
            if len(RNE) != 3:
                raise ValueError
            if any(x < 0 or x > 100 for x in RNE):
                raise ValueError
            if all(isinstance(x, int) for x in RNE):
                self.__RNE = RNE
            else:
                raise ValueError
        else:
            raise ValueError

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return (randint(0, 100) for _ in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"

    # проверка, является ли имя именем
    @staticmethod
    def __check_name(name):
        if isinstance(name, str):
            if name.isalpha():
                raise ValueError
            # первая буква должна быть большой
            return name.capitalize()
        else:
            raise ValueError

    def get_number(self):
        return self.__number

    def get_status(self):
        return self.__check()


module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))

# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))

# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))


## Задача 2


from random import *


class InvalidAction(Exception):
    pass


class Emerald:
    __statuses = ["не учтён", "учтён", "отправлен под спуд"]

    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0

        # цена изумруда
        self.__price = 0

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.price = randint(5, 15) * 10
        else:
            raise InvalidAction

    def store(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise InvalidAction

    @property
    def status(self):
        return Emerald.__statuses[self.__status]

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise InvalidAction

    def __str__(self):
        return "Изумруд"


class Shell:
    __statuses = ["не учтена", "учтена",
                  "отправлена в монетолитейное отделение",
                  "переплавлена в монету"]

    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = 0

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.price = randint(3, 10)
        else:
            raise InvalidAction

    def process(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise InvalidAction

    def smelt(self, archive):
        if self.__status == 2:
            self.__status = 3

            # пример реализации (можно придумать свой)
            # генерируем монеты с номиналом 5
            for i in range(self.__price // 5):
                archive.add(Entry(Coin(Coin.next_serial, "2023", 5)))
                Coin.next_serial += 1

            # генерируем монеты с номиналом 1
            for i in range(self.price % 5):
                archive.add(Entry(Coin(Coin.next_serial, "2023", 1)))
                Coin.next_serial += 1
        else:
            raise InvalidAction

    @property
    def status(self):
        return Shell.__statuses[self.__status]

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise InvalidAction

    def __str__(self):
        return "Золотая скорлупка"


class Coin:
    next_serial = 0

    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number

        # год выпуска монеты
        self.__year = year

        # номинал монеты
        self.__value = value

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def year(self):
        return self.__year

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return "Монета"


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []

    def add(self, entry):
        if isinstance(entry, Entry):
            self.__storage.append(entry)
        else:
            raise InvalidAction

    def get(self, index):
        entry = self.__storage[index]

        if entry == None or entry.secret:
            return f"[Запись {index}] Информация удалена"

        item = entry.item
        result = f"[Запись {index}-{entry.ID}] "
        result += f"[{str(item)}] {entry.date} '{entry.info}' "
        if isinstance(item, Emerald) or isinstance(item, Shell):
            result += f"Статус: {item.status} Цена: {item.price} "
        elif isinstance(item, Coin):
            result += f"Серийный номер: {str(item.serial_number).zfill(6)} "
            result += f"Год выпуска: {item.year} "
            result += f"Номинал: {item.value}"
        return result

    def edit(self, index, info):
        self.__storage[index].info = info

    def classify(self, index):
        self.__storage[index].secret = True

    def declassify(self, index):
        self.__storage[index].secret = False

    def delete(self, index):
        self.__storage[index] = None

    def info(self):
        for i in range(len(self.__storage)):
            print(self.get(i))

    def item(self, index):
        return self.__storage[index].item


class Entry:
    def __init__(self, item, date="01.01.2023", info="", secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()

        # указатель на объект
        self.__item = item

        # дата создания записи
        self.__date = date

        # дополнительная информация об объекте
        self.__info = info

        # информация засекречена?
        self.__secret = secret

    def __get_next_ID(self):
        # можно создать свою функцию вместо этой
        return hash(self)

    @property
    def ID(self):
        return self.__ID

    @property
    def item(self):
        return self.__item

    @property
    def date(self):
        return self.__date

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info = info

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, update):
        if isinstance(update, bool):
            self.__secret = update
        else:
            raise InvalidAction


archive = Archive()
for _ in range(20):
    shell = Shell()
    shell.account()

    archive.add(Entry(shell))

archive.info()

for _ in range(10):
    emerald = Emerald()
    emerald.account()

    archive.add(Entry(emerald))

archive.info()

for i in range(20, 30):
    archive.item(i).store()

archive.info()

for i in range(20):
    archive.item(i).process()

archive.info()

for i in range(20):
    archive.item(i).smelt(archive)

archive.info()

for i in range(20, 30):
    archive.classify(i)

archive.info()

for i in range(20):
    archive.delete(i)

archive.info()

for i in range(25, 30):
    archive.declassify(i)

archive.info()

for i in range(25, 30):
    archive.edit(i, "Информация обновлена")

archive.info()

i = 30
try:
    while True:
        print(archive.get(i))
        i += 1
except IndexError:
    pass
