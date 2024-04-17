import requests

from dotenv import find_dotenv, load_dotenv
import os

env_path = find_dotenv('.env')  # os.path.join(os.path.dirname(__file__), 'Что такое API. Практика', '.env') - ещё так
load_dotenv(dotenv_path=env_path)


def amount_calculation(currency_rate, amount):  # счет суммы, введенной пользователем
    return currency_rate * amount


def check_course(value='RUB', base_currency='USD', amount=1):
    api_key = os.getenv('API_KEY_FOR_FREECURRENCYAPI')
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&base_currency={base_currency}&currencies={value}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            currency_rate = data["data"][f"{value}"]  # считаем базовый курс валют за 1 еденицу
            final_exchange = amount_calculation(currency_rate, amount)  # считаем теперь сумму
            print(f'Отношение значения {amount} {base_currency} в {value} этой суммы будет: {final_exchange} {value}')
        else:
            print(f'Соединение с сайтом не установлено, статус код операции {response.status_code}')
    except requests.exceptions.RequestException as g:
        print(f'Не удалось соединиться с сайтом, чтобы направить туда клиентский запрос, ошибка: {g}')


try:  # ловим некорректную сумму
    print('Введите исходную валюту:')
    base_currency = input()
    print('Введите валюту, куда собираемся конвертировать сумму:')
    target_value = input()
    print('Ввод суммы исходной валюты:')
    amount = float(input())
    check_course(target_value, base_currency, amount)
except TypeError:
    print(f'Введена некорректная сумма, она должна быть в виде последовательности чисел')
