import requests


def check_weather(city):
    api_key = 'f3ad9ed01a7748c4a7d152603241002'  # регаемся на сайте, чтобы получить свой уникальный ключ
    url = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=ru'  # дополняем query string своими
    try:  # параметрами, читая документацию данного API
        response = requests.get(url)
        if response.status_code == 200:
            data_weather = response.json()  # получаем ответ в формате JSON
            print(
                f'Погода в {city} на момент {data_weather["current"]["last_updated"]} составляет {data_weather["current"]["temp_c"]} градусов цельсия,'
                f' а конкретно сейчас'
                f' - {data_weather["current"]["condition"]["text"]}')  # предварительно смотрим словарь, чтобы правильно
        else:  # обратиться к нужным данным
            print(f'{url} недоступен. Попробуйте позднее.')  # ловим возможные ошибки после прошедшего реквеста
    except requests.exceptions.RequestException as g:  # ловим возможные ошибки на этапе реквеста
        print(f'{url} недоступен, не удалось установить соединение с сайтом для отправки запроса. Ошибка: {g}')


check_weather('Moscow')
