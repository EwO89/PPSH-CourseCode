

## Задача 2


import black


def format_dna_analyzer(file_path):
    # Читаем содержимое исходного файла
    with open(file_path, "r") as file:
        dna_code = file.read()

    # Форматируем код с помощью Black
    formatted_code = black.format_str(dna_code, mode=black.FileMode())

    # Записываем отформатированный код обратно в файл
    with open(file_path, "w") as file:
        file.write(formatted_code)


# Пример использования функции
file_path = input("Ввидет путь до файла, который хотите отформатировть: ")
format_dna_analyzer(file_path)
print("Файл успешно отформатирован")
