import requests  # чтобы отправлять запросы с сайтов и получать с них ответы
import os  # для взятия переменной нужной с env
from dotenv import find_dotenv, load_dotenv  # используем виртуальныее переменные обязательно для безопасности
from concurrent.futures import ThreadPoolExecutor  # используем принцип параллелизма для данной задачи,
import time  # чтобы замерить время работы скрипта на скачку фоток
from PIL import Image  # длля создания гиф анимации

path_env = find_dotenv('.env')
load_dotenv(dotenv_path=path_env)  # нашли и подгрузили .env

count_of_images = 0  # считаем количество успешно скачанных фоток


def download_image(image_url, template_file, number):
    global count_of_images  # функция для закачки фоток с обработанных данных
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(template_file, 'wb') as file:  # сохраняем в моде wb - для изображений
                file.write(response.content)

                count_of_images += 1
            print(f'Фотка с порядковым номером {number} сохранена в файл: {template_file}')
        else:
            print(f'Ошибка отправки ответа на скачивание файла {template_file}. Статус код: {response.status_code}')
    except requests.exceptions.RequestException as err:
        print(f'Не удалось подключиться к сайту. Ошибка: {err}')


def parallel_mode(list_urls_image, images_earth_template_name_file):  # параллельный режим enable
    with ThreadPoolExecutor(max_workers=None) as executor:  # None- т.к. система оптимально найдет сколько нужно потоков
        for i, image_url in enumerate(list_urls_image):  # создаем кортеж из индекса и самой ссылки
            template_file = f'{images_earth_template_name_file}_{i}.png'  # создали шаблон файлов будущих
            executor.submit(download_image, image_url, template_file, i)  # создаем элементы Future, параллелим скачку


def download_earth_image(date, images_earth_template_name_file):  # функция для обработки данных и скачки фоток

    api_key = os.getenv('API_KEY_FOR_APINASA')  # подгружаем с помощью OS нужную переменную из env
    url = f'https://api.nasa.gov/EPIC/api/natural/date/{date}?api_key={api_key}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            images_data = response.json()
            # Подготовка URL для скачивания изображений
            first_image_date = images_data[0]['date'][0:10].replace('-',
                                                                    '/')  # нашли дату и отформатировали под запрос
            template_url = f'https://api.nasa.gov/EPIC/archive/natural/{first_image_date}/png'  # создали шаблон url img
            list_urls_image = [f'{template_url}/{img["image"]}.png?api_key={api_key}' for img in images_data]  # список
            # ссылок на фотки
            # Используем ThreadPoolExecutor для параллельного скачивания (чтобы было быстрее, несколько запросов сразу)
            st = time.time()
            parallel_mode(list_urls_image, images_earth_template_name_file)
            fn = time.time()
            print(f'скачивание фотографий с сайта прошло за {fn - st} секунд')
        else:
            print(f'Не удалось  получить данные о дате. Статус код: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to the site. Error: {e}')


images_earth_template_name_file = 'secret_pictures'
download_earth_image('2022-07-07', images_earth_template_name_file)


def gif():  # после работы основного блока кода создаем нашу гифку
    global count_of_images
    photos = []
    for num in range(count_of_images):  # по порядку загружаем объекты изображения
        photo = Image.open(f'secret_pictures_{num}.png')  # то есть создаем промежутные объекты для создания
        photos.append(photo)  # гиф анимации

    photos[0].save(  # photos[0] - задали старт для начала гифки
        'earth.gif',  # даем название нашему гиф файлу
        save_all=True,  # подключаем все фотки из списка фотос в одну гифку общую
        append_images=photos[1:],  # продолжаем склеивать фотки по порядку со 2 элемента до конца
        optimize=True,  # делаем оптимальный размер нашей гифки
        duration=200,  # минимальная задержка между кадрами в нашей гиф анимации
        loop=0  # циклим нашу гифку на бесконечность
    )
    print('Ваша gif была сформирована!')

gif()
