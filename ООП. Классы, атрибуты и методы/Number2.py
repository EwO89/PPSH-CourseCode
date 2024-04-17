class PhotoCamera:
    'Этот класс вносит в нашу базу данных различные фотокамеры'

    def __init__(self, brand, model, resolution, is_on, memory_capacity=0):
        self.brand = brand
        self.model = model
        self.resolution = f'{resolution[0]}x{resolution[1]}'   #  распаковали введенные данные пользователем о нашем разрешении
        self.is_on = is_on
        self.memory_capacity = memory_capacity
        self.photos = []  # будем считать, что наши фотографии все весят по 1 мб (волшебная камера), как и введенное место в мемори будет в мб для проверки места

    def take_photo(self):
        if self.is_on:
            return f'Сделана фотография с разрешением {self.resolution}'
        else:
            return f'сначала включите камеру'

    def get_camera_info(self):
        return f'Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution}'

    def turn_on(self):
        if self.is_camera_on():
            return f'Фотокамера и так включена'
        else:
            self.is_on = True
            return f'Фотокамера выключена'

    def turn_off(self):
        if self.is_camera_on():
            self.is_on = False
            return f'Фотокамера выключена'
        else:
            return f'Фотокамера и так выключена'

    def is_camera_on(self):
        if self.is_on:
            return True
        else:
            return False

    def store_photo(self, photo):
        if len(self.photos) < self.memory_capacity:
            self.photos.append(photo)
            return True
        else:
            return False

    def view_photos(self):
        if self.photos:
            print('Ваш список сохранённых фотографий:')
            for i in range(len(self.photos)):
                print(f'{i + 1}: {self.photos[i]}')
        else:
            print('В памяти нет фотографий')

    def clear_memory(self):
        self.photos = []
        print('Вы очистили память от фотографий')


model_1 = PhotoCamera('Samsung', '22A', [int(input()) for x in range(2)], True,
                      memory_capacity=5000)  #  просто ручной пример, что все работает, а лист компрехеншеном ставим разрешение
print(model_1.take_photo())
print(model_1.get_camera_info())
print(model_1.turn_off())
print(model_1.is_camera_on())
print(model_1.store_photo('Фотка с 2018 года.png'))
model_1.view_photos()
model_1.clear_memory()
model_1.view_photos()
print(PhotoCamera.__doc__)