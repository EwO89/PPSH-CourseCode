## Задача 1



class EmployeeInfo:
    def __init__(self, name, employee_id, position, mail):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.mail = mail

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Mail: {self.mail}")


class EmployeeMail:
    def generate_email(self):
        email = f"{self.name.lower().replace(' ', '.')}.{self.employee_id}@company.com"

    return email


def send_email(self, recipient, subject, message):
    print(f"Sending email to {recipient}:\nSubject: {subject}\nMessage: {message}")




## Задача 2




class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        pass


class FAVDiscount(Discount):
    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return self.price * 0.4




## Задача 3


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)




## Задача 4


from abc import ABC, abstractmethod


class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimmable(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Crow(Walkable, Flyable):
    def walk(self):
        pass

    def fly(self):
        pass


class Penguin(Walkable, Swimmable):
    def walk(self):
        pass

    def swim(self):
        pass




## Задача 5


from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Lamp(Device):
    def turn_on(self):
        print("Lamp turned on")

    def turn_off(self):
        print("Lamp turned off")


class MotionSensor(Device):
    def turn_on(self):
        print("Motion sensor turned on")

    def turn_off(self):
        print("Motion sensor turned off")


class Thermostat(Device):
    def turn_on(self):
        print("Thermostat turned on")

    def turn_off(self):
        print("Thermostat turned off")


class SmartHome(Device):
    def __init__(self, devices):
        self.devices = devices

    def turn_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_off(self):
        for device in self.devices:
            device.turn_off()




## Задача 6

from abc import ABC, abstractmethod


class Transferable(ABC):
    @abstractmethod
    def transfer(self, destination_account, amount):
        pass


class TransferService:
    def __init__(self, source_account, destination_account):
        self.source_account = source_account
        self.destination_account = destination_account

    def transfer(self, amount):
        self.source_account.transfer(self.destination_account, amount)


class Account(Transferable):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        return self.balance

    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            destination_account.deposit(amount)
        else:
            raise ValueError("Insufficient balance for transfer")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    def get_interest_rate(self):
        return self.interest_rate


class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, fee_percentage=0):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        fees = self.balance * (self.fee_percentage / 100)
        self.balance -= fees

    def get_fee_percentage(self):
        return self.fee_percentage


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        if self.find_account(account.account_number):
            self.accounts.remove(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer_funds(self, source_account_number, destination_account_number, amount):
        source_account = self.find_account(source_account_number)
        destination_account = self.find_account(destination_account_number)

        if source_account and destination_account:
            transfer_service = TransferService(source_account, destination_account)
            transfer_service.transfer(amount)
        else:
            raise ValueError("Source or destination account not found")



