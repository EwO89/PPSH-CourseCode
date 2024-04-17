import requests


def Download_Image(url, file):
    try:
        responce = requests.get(url)  # получили ответ от сервера
        responce.raise_for_status()   # подняли статус сервера, чтобы словить если что ошибку
        with open(file, 'wb') as g:   # методом wb в файл наш созданный подгружаем сторонний контент
            g.write(responce.content)  # метод wb - подгружает файлы в бинардном виде в виде байтов, контент добавился
            print(f'скачивание в файл {g} прошло успешно')  # в виде потока байтов закодировалось изображение
    except requests.exceptions.Timeout:   # из библиотеки запросов достаем модуль ошибок, какую-ту на выбор ловим
        print(f'Извините, но у вас ошибка: истекло время подключения, повторите позднее')
    except requests.exceptions.ConnectionError:
        print(f'Извините, но не удалось установить соединение с сервером, попробуйте ещё раз')


url = 'https://storage.theoryandpractice.ru/tnp/uploads/image_block/000/052/014/image/base_d9dd9b626f.jpg'
file = 'secret_file.jpg'
Download_Image(url, file)
