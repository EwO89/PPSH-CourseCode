# Пакетные менеджеры. Домашнее задание.

> В данном ДЗ Вам нужно попробовать самостоятельно прочитать документацию и попробовать решить задачу через незнакомую библиотеку. Если Вам тяжело, то не беспокойтесь, с некоторыми библиотеками мы встретимся на следующей неделе и к этому ДЗ можно будет вернуться ещё раз.

## Задача 0

Установите библиотеку `howdoi` и разберитесь с тем, как она работает. Она может помочь вам задавать вопросы в командной строке, не обращаясь к гуглу.

## Задача 1

Используя библиотеку `requests` напишите программу, которая должна запрашивать у пользователя URL-адрес веб-страницы и выводить на экран статус запроса (успешно или нет) и код состояния HTTP-ответа.

## Задача 2

Используя библиотеку `Pillow`, напишите программу, которая будет загружать изображение, изменять его размер и сохранять измененное изображение.

## Задача 3 

Используя библиотеку `pytube`, напишите программу, которая запрашивает у пользователя URL YouTube видео и сохраняет его в ту же папку, где находится сам питоновский файл. Если скачивание прошло успешно, на экран выводится сообщение об этом. Если произошла ошибка, тогда выводится сообщение об ошибке.

## Задача 4

Используя библиотеку `colorama`, напишите программу, которая бы выводила четыре строки, покрашенные в разные цвета, в консоль в следующих форматах:

- сам текст покрашен в какой-то цвет;
- сам текст + его фон покрашен в какой-то цвет;
- снова текст, но без какого-либо окрашивания;
- сам текст с покрашенным фоном в какой-то цвет.

> Сами строки могут быть любыми. Здесь важен цвет, а не содержимое строки :)

## Задача 5

Используя библиотеку `emoji`, преобразуйте эмозди в строке ниже в текстовый формат:

```raw
'Buy 📈📈📈 the programming after 👀 school 👏📚🏫 course! 😂'
```

Пример текстовой записи для эмодзи:

```raw
👀 -> :eyes:
```

> Это может быть полезно для обработки текста или при использовании кодировки, которая не поддерживает эмодзи.

## Задача 6

Используя библиотеки `pyperclip` и `time`, напишите программу, которая бесконечно работает и каждую секунду преобразует строку в буфере обмена по следующим правилам:

- все лишние пробелы между словами и в конце/начале строки убираются;
    - `  Hello \n   world!\n   \t\t` преобразуется в `Hello world!`
- все буквы `ё` заменяются на буквы `е`;
- все заглавные буквы заменяются на строчные.

## Задача 7

Используя библиотеку `wikipedia`, выведите на экран основную информацию о том, что такое компьютерная программа (`Computer program`).