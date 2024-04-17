import requests  # API для взаимодействия с сервером
from bs4 import BeautifulSoup  # Библиотека для анализа HTML страницы с последующим парсингом
import random  # Библиотека для вывода рандомированных запаршенных цитат


def extracion_quote_on_website(urls, secret_file_anime):
    citations = []
    for url in urls:  # у меня один сайт в подборке, но есть возможность несколько сайтов посмотреть
        try:
            response = requests.get(url)  # получили ответ от сайта
            if response.status_code == 200:
                extraction_html = BeautifulSoup(response.content, 'lxml')  # извлекаем html страницу для анализа
                quotes_on_website = extraction_html.find_all('div', class_='field-item even last')  # нашел класс, в
                for quote in quotes_on_website:  # котором собраны наши цитаты на сайте
                    citations.append(quote.text.strip())  # из списка собранных элементов получаю его расшифровку txt
                citations = [citation for citation in citations if not any(char.isdigit() for char in citation)]
                # убрал мусор, который не является цитатой, но был в классе. Понял, что мусор только там, где цифры
            else:
                print(f'{url} недоступен. Попробуйте позднее. Статус код операции : {response.status_code}')
        except requests.exceptions.RequestException as g:
            print(f'Не удалось установить соединение с сайтом. Ошибка: {g}')
    with open(secret_file_anime, 'w', encoding='utf-8') as file:
        for quote in citations:
            file.write(quote + '\n')  # запись в файл цитат, не забываю элементы отделять через /n


def random_choise_quote(file):  # как только файл с цитатами готов, рандомим цитаты для вывода
    with open(file, 'r', encoding='utf-8') as p:
        citation = p.readlines()
        print(random.choice(citation).rstrip())


anime_urls = ['https://citaty.info/anime']
secret_file_anime = 'secret_anime_file.txt'
extracion_quote_on_website(anime_urls, secret_file_anime)
random_choise_quote(secret_file_anime)
