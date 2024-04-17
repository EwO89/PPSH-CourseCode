import random


class Revolver:
    ' Этот класс помогает пользователю взаимодействовать с револьером '
    def __init__(self, index=0, all_items=False):
        self.drum = [''] * 6
        self.index = index  # указатель за current_bullet
        self.all_items = all_items
        self.current_bullet = None  # Изначально курок никуда не направлен, ведь нет патронов в барабане

    def add_bullet(self):
        for i in range(len(self.drum)):
            if self.drum[i] == '':
                self.drum[i] = f'bullet {i + 1}'
                self.current_bullet = self.drum[i]
                self.index = i
                return True
        return False

    def add_bullets_from_list(self, *bullets, index_for_bullets_to_add=0):  # Идейно мы проверяем разные случаи
        bullets_to_add = list(bullets)
        length_bullets_to_add = len(bullets_to_add)
        if length_bullets_to_add == 0:  # когда список пуст
            return False
        elif '' not in self.drum:
            return f'У вас полностью заряжен барабан. Разрядите его, чтобы иметь возможность его пополнить'
        for i in range(len(self.drum)):
            if self.drum[i] == '' and len(bullets_to_add) != 0:
                self.drum[i] = f'bullet {i + 1}'
                bullets_to_add.pop(index_for_bullets_to_add)
            elif (len(bullets_to_add) == 0) or ('' not in self.drum):  # заполнение барабана, но стало некуда заполнять
                return True  # + когда закончились патроны в списке
        return True

    def shoot(self):
        old = self.drum[self.index]
        self.drum[self.index] = ''
        try:
            self.index -= 1
            if self.drum[self.index] == '':
                raise ValueError("Барабан разряжен")
            else:
                self.current_bullet = self.drum[self.index]
                return f'Сделал выстрел с дроби!'
        except ValueError:
            self.index = 0
            self.current_bullet = None
            return None

    def all_items_enable(self):        # Ввел две дополнительные функции
        self.all_items = True            # Чтобы по запросу вкл или выкл

    def all_items_off(self):
        self.all_items = False

    def unload(self):
        if self.all_items:
            return self.drum
        else:
            if self.current_bullet is None:
                return None
            else:
                return self.current_bullet

    def scroll(self):      # из модуля рандом достали шафл,
        new_drum = self.drum  # чтобы в новом объекте с текущим барабаном все перемешать,
        random.shuffle(new_drum) # а затем переприсвоить текущий индекс к новому списку,
        self.current_bullet = new_drum[self.index]  # типа якобы мы сделали перемешку, но остались на текущем месте

    def bullet_count(self):
        return len([bullet for bullet in range(len(self.drum)) if self.drum[bullet] != ''])

#  Тесты всех случаев на нашем первом экземпляре
model_1 = Revolver()
print(model_1.current_bullet)
print(model_1.add_bullet())
print(model_1.current_bullet)
print(model_1.add_bullet())
print(model_1.shoot())
print(model_1.current_bullet)
print(model_1.all_items_enable())
print(model_1.unload())
print(model_1.scroll())
print(model_1.current_bullet)
print(model_1.bullet_count())
print(model_1.shoot())
print(model_1.shoot())
print(model_1.add_bullets_from_list(1, 2, 3, 4, 5, 6, 7))
print(model_1.bullet_count())
