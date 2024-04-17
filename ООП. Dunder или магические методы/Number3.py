class Item:

    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        self.rarity = rarity
        self.color = color

    def __gt__(self, other):  # >
        if self.ID > other.ID:
            return True
        if self.price > other.price:
            return True
        if self.rarity > other.rarity:
            return True
        if self.color > other.color:
            return True
        return False

    def __le__(self, other):  # <=
        return self == other or self < other  # для вызова операторов __lt__ __eq__

    def __lt__(self, other):  # <
        return not self > other

    def __ge__(self, other):  # >=
        return self > other or self == other  # обращаемся к определенный операторам

    def __ne__(self, other):  # !=
        return not self == other

    def __eq__(self, other):  # ==
        return self.ID == other.ID and self.price == other.price and self.rarity == other.rarity and self.color == other.color

    def __str__(self):  # для вывода в понятном виде для нас нашего ответа
        return f'Ваш экземпляр: {self.ID, self.price, self.rarity, self.color}'


new_item = Item(128, 500, 1, "FF5819")
new_item1 = Item(128, 500, 2, "BB5819")
new_item2 = Item(128, 200, 4, "FF5812")
new_item3 = Item(129, 498, 1, "FF5812")
instances = [new_item, new_item1, new_item2, new_item3]
d = (list(sorted(instances, reverse=True)))  # делаем слева-направо отображение важных предметов
print(*d)  # распаковали лист, чтобы вывести его содержимое
