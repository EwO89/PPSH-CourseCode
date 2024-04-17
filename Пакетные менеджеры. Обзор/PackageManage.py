
## Задача 1


import requests

url = input("Введите URL-адрес веб-страницы: ")
response = requests.get(url)

if response.status_code == 200:
    print("Запрос выполнен успешно!")
else:
    print("Ошибка при выполнении запроса.")

print("Код состояния HTTP-ответа:", response.status_code)


## Задача 2


from PIL import Image

image = Image.open("image.jpg")
resized_image = image.resize((800, 600))
resized_image.save("resized_image.jpg")

image.close()


## Задача 3
from pytube import YouTube

def download_video(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    try:
        video.download()
    except:
        print("Произошла ошибка.")
    print("Скачивание успешно.")

link = input("Введите URL на YouTube видео: ")
download_video(link)


## Задача 4

В консоли запускаете этот файл, тогда цвета должны правильно отображаться (в IDLE и в других средах для разработки может не работать).


from colorama import init, Fore, Back, Style

init()
print(Fore.RED + 'красный текст')
print(Back.GREEN + 'красный текст с зелёным фоном')
print(Style.RESET_ALL + 'обычный текст')
print(Back.GREEN + 'текст c зелёным фоном')


## Задача 5


from emoji import demojize

promo_text = 'Buy 📈📈📈 the programming after 👀 school 👏📚🏫 course! 😂'
result = demojize(promo_text)
print(result)


## Задача 6

from pyperclip import copy, paste
from time import sleep

while True:
    text = paste()
    text = " ".join(text.split()).replace("ё", "е").lower()
    copy(text)
    sleep(1)


## Задача 7


import wikipedia
result = wikipedia.page("Computer program")
print(result.summary)
