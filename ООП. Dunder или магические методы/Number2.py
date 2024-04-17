class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.y)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - self - other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return f'Координаты вашего вектора: {self.x, self.y, self.z}'

    def __eq__(self, other):
        return (self.__abs__() == other.__abs__()) and (Vector3.f(self, other) > 0)

    def f(self, other):  # для проверки сонаправленности
        return self.x * other.x + self.y * other.y + self.z + other.z

    def __ne__(self, other):
        return self.__abs__() != other.__abs__()

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'Координаты вашего вектора: {self.x, self.y}'

    def __eq__(self, other):
        return (self.__abs__() == other.__abs__()) and (Vector2.f(self, other) > 0)

    def f(self, other):  # для проверки сонаправленности
        return self.x * other.x + self.y * other.y

    def __ne__(self, other):
        return self.__abs__() != other.__abs__()

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


d = Vector2(6, 8)
q = Vector2(6, 8)
r = d == q
print(r)
print(str(d))
