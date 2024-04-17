import requests  # для получения API стороннего сервиса
from matplotlib import pyplot as plt  # для рисования графика подмножества ax
from datetime import datetime  # для форматирования дат для библиотеки matplotlib
from matplotlib import dates as mdates  # для создания связи между метками на OX и OY
import os  # для взятия нужной виртуальной переменной из .env
from dotenv import find_dotenv, load_dotenv  # для подгрузки .env

env_path = find_dotenv('.env')  # подгружаем виртуальные переменные для безопасности personal data
load_dotenv(dotenv_path=env_path)


def check_weather(city, days):
    api_key = os.getenv('API_KEY_FOR_APIWEATHER')
    url = f'https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&lang=ru&days={days}'  # читал doc для
    try:  # correct query string
        response = requests.get(url)
        if response.status_code == 200:
            data_weather = response.json()
            dates = [data['date'] for data in data_weather['forecast']['forecastday']]  # извлечение нужных data
            avgtemp_c = [avgtemp_c['day']['avgtemp_c'] for avgtemp_c in data_weather['forecast']['forecastday']]
            dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]  # для создания нужных дат для графика
            results_extract_data_of_weather(dates, avgtemp_c, city, days)  # строим график
    except requests.exceptions.RequestException as g:  # обработка захода на сайт
        print(f'Сайт недоступен. Ошибка: {g}')


def results_extract_data_of_weather(dates, avgtemp_c, city, days):
    fig, ax = plt.subplots(nrows=1, ncols=1)  # создаем fig (все пространство) и ax (один график в данном случае)
    ax.plot(dates, avgtemp_c, marker='.', label='Средняя температура', linestyle='-', color='purple')  # редачим график
    ax.xaxis.set_major_locator(mdates.DayLocator())  # ищем разделители и делаем связь между осями
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%y'))  # форматируем элементы оси OX
    plt.title(f'Средняя температура в {city} на следующие {days} дней ')  # установка заголовка графика
    plt.xticks(rotation=45)  # поворачиваем элементы оси OX под нужным углом для красивого отображения
    plt.xlabel('Дата')  # Озаглавим ось OX
    plt.ylabel('Средняя температура')  # заглавим ось OY
    plt.grid(which='major')  # делаем сетку для лучшей визуализации
    plt.legend(loc='upper left')  # отображение легенды (помогает различить, какой набор данных соответствует каждой
    plt.tight_layout()  # чтобы элементы графика не перекрывались друг другом
    plt.show()  # линии или символу на графике - метод визуализации.
    # plt.show() - показывает график


print('Прогноз погоды какого города Вы хотите узнать?')
city = input()
print('Сколько дней прогноза Вас интерисует?')
days = int(input())
check_weather(city, days)
