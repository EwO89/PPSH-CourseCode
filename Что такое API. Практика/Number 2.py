import requests


def check_website(urls):
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{url} доступен.")
            else:
                print(f"{url} недоступен.Статус код: {response.status_code}")
        except requests.exceptions.RequestException as g:  # если не удалось установить соединение с сервером
            print(f" Ошибка:", g)  # ну т.е.  не дошло дело до респонса от сервера


urls = ['https://github.com', 'https://osel.ru']
check_website(urls)
