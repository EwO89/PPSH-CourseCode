

## Задача 1



class HeavenlyBody:
    'Родительский класс Planet'

    def __init__(self, name, age, temperature, radius):
        self.name = name
        self.age = age
        self.temperature = temperature
        self.radius = radius

    def display(self):
        print(f'Название: {self.name}')
        print(f'Возраст: {self.age} (млн. лет)')
        print(f'Температура: {self.temperature} (С)')
        print(f'Радиус: {self.radius} (км)')


class Planet(HeavenlyBody):
    'Дочерний класс Planet'

    def __init__(self, name, age, temperature, radius, orbital_speed):
        super().__init__(name, age, temperature, radius)
        self.orbital_speed = orbital_speed

    def display(self):
        super().display()
        print(f'Орбитальная скорость: {self.orbital_speed} (км/с) \n')


class Star(HeavenlyBody):
    'Дочерний класс Star'

    def __init__(self, name, age, temperature, radius, constellation):
        super().__init__(name, age, temperature, radius)
        self.constellation = constellation

    def display(self):
        super().display()
        print(f'Созвездие: {self.constellation} \n')




## Задача 2

import datetime


class Pastry:
    def __init__(self, name, price, manufacture_date, term):
        self.id = id(self)
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def display(self):
        print(f'Название: {self.name}')
        print(f'Цена: {self.price} (руб.)')
        print(f'Дата изготовления: {self.manufacture_date}')

    def valid_until(self):
        today = datetime.date.today()
        end_date = self.manufacture_date + datetime.timedelta(days=self.term)
        remaining_time = end_date - today
        if remaining_time.days < 0:
            return 'Срок годности истек'
        else:
            return 'Срок годности истекает через {} дня'.format(remaining_time.days)


class Cake(Pastry):
    def __init__(self, name, price, manufacture_date, term, filling):
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def order(self):
        Cake.display(self)
        print(f'Начинка: {self.filling}')
        if Cake.valid_until(self) != 'Срок годности истек':
            print(Cake.valid_until(self))
            print(f'Оформлен заказ {self.id} - {self.name} с начинкой {self.filling} \n')
        else:
            print('Нет в наличии! Выберите другую позицию')


class BentoCake(Pastry):
    def __init__(self, name, price, manufacture_date, term, celebration):
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def order(self):
        if BentoCake.valid_until(self) != 'Срок годности истек':
            BentoCake.display(self)
            print(f'Праздник: {self.celebration}')
            print(BentoCake.valid_until(self))
            print(f'Оформлен заказ {self.id} - {self.name} на {self.celebration} \n')
        else:
            print('Нет в наличии! Выберите другую позицию')




## Задача 3



class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self._balance = balance
        self._interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, holder):
        self.__holder = holder

    def __str__(self):
        print(f'Владелец: {self.__holder}')
        print(f'Баланс: ${self._balance:,.2f}')
        print(f'Процентная ставка: {self._interest_rate} \n')


class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.id = id(self)
        self.transactions = []

    def deposit(self, amount):
        self._balance += amount
        self.transactions.append(f'Аккаунт {self.id} - внесение наличных на счет: ${amount:,.2f}')

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            self.transactions.append(f'Аккаунт {self.id} - cнятие наличных: ${amount:,.2f}')
        else:
            print('Аккаунт {self.id} - недостаточно средств на счете')

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        self.transactions.append(f'Аккаунт {self.id} - начислены проценты по вкладу: ${interest:,.2f}')

    def history(self):
        for transaction in self.transactions:
            print(transaction)




## Задача 4


#сделал в notion




## Задача 5

from abc import *

class Investments:
    def __init__(self, ticker, price, currency, industry):
        self.ticker = ticker
        self.price = price
        self.currency = currency
        self.industry = industry

    def display(self):
        print(f'Тикер: {self.ticker}')
        print(f'Цена: {self.price}')
        print(f'Валюта: {self.currency}')
        print(f'Сектор: {self.industry}')

    @abstractmethod
    def buying(self):
        pass


def buying_securities(func):
    def wrapper(security):
        if security.echelon == 3:
            print('Это высокорискованная сделка \n')
            return None
        return func(security)

    return wrapper


class Shares(Investments):
    def __init__(self, ticker, price, currency, industry, dividend, echelon, profit):
        super().__init__(ticker, price, currency, industry)
        self.dividend = dividend
        self.echelon = echelon
        self.profit = profit

    @buying_securities
    def buying(self):
        if self.profit > 5:
            lot = int(input('Количество: '))
            print(f'Совершена покупка на сумму: {self.price * lot}. Поздравляю Вы стали совладельцем компании!')
        else:
            print('Это высокорискованная сделка \n')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self.coupon = coupon
        self.echelon = echelon
        self.nominal = nominal

    @buying_securities
    def buying(self):
        if self.price <= self.nominal:
            lot = int(input('Количество: '))
            print(f'Совершена покупка на сумму: {self.price * lot}. Поздравляю Вы стали кредитором компании!')
        else:
            print('Это высокорискованная сделка \n')



