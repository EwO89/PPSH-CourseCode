import os  # взять переменную виртуальную
import requests  # судя по документации, можно и через запрос, так что оставим
import nlpcloud  # для работы с этим API
from dotenv import find_dotenv, load_dotenv  # поиск env

path_env = find_dotenv('.env')
load_dotenv(dotenv_path=path_env)  # нашли env


def download_image(file, image_link):  # настраиваем скачку этой фотки по стандарту
    response = requests.get(image_link)
    try:
        if response.status_code == 200:
            with open(file, 'wb') as g:  # wb - метод скачки изображений
                g.write(response.content)
        else:
            print(f'Обратный ответ не последовал. Статус код операции: {response.status_code}')
    except requests.exceptions.RequestException as f:
        print(f'Не удалось соединиться с сайтом. Ошибка {f}')


def generate_image(text, file):
    apy_key = os.getenv('API_KEY_FOR_NLPCLOUD')
    client = nlpcloud.Client("stable-diffusion", apy_key, True, 'ru')  # stable-diffusion - модель, делающая фотку
    image_link = client.image_generation(text)  # генерируем изображение на основе созданного элемента клиента
    download_image(file, image_link)


file = 'Thanos and Vinny.png'  # сюда кладём файл
#  Битва Таноса и Винни-Пуха
text = input()  # лучше на английском давать запрос
generate_image(text, file)
