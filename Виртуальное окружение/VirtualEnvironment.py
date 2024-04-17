## Задача 6


from win11toast import toast
dir(toast)
help(win11toast.toast)

from win11toast import toast
from datetime import datetime

def validate_time(alarm_time):
    if len(alarm_time) != 5:
        return 'Неверный формат'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Неверный формат часов'
        elif int(alarm_time[3:5]) > 59:
            return 'Неверный формат минут'
        else:
            return True

while True:
    alarm_time = input("Укажите время будильника в формате 'HH:MM' \nВремя будильника: ")
    validate = validate_time(alarm_time)
    if validate:
        name = input('Введите название: ')
        print(f'Будильник установлен на время {alarm_time}')
        break
    else:
        print(validate)

alarm_HH = int(alarm_time[0:2])
alarm_MM = int(alarm_time[3:5])

while True:
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    if alarm_HH == current_hour:
        if alarm_MM == current_min:
            toast('Будильник', name, button='Выключить', audio='C:\Windows\Media\Alarm01.wav')
            break



# остальное в notion (задачи)