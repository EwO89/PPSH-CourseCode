class SignedMessage:
    def __new__(cls, *args):
        cls.infiltrate()
        return object.__new__(cls)

    def __init__(self, message, structure):
        self.message = message
        self.structure = structure

    def __str__(self):
        return f'Ваше сообщение, рядом крутая подпись: {self.message} {self.structure}'

    def __add__(self, other):
        return f'Ваше сдвоенное сообщение :{self.message + other.message} {self.structure}'

    @staticmethod
    def infiltrate():
        pass


SIGNATURE = "-~=$([{PETR}])$=~-"
q = SignedMessage("Hello ", SIGNATURE)
d = SignedMessage("world!", SIGNATURE)
r = d + q
print(r)
print(str(q))