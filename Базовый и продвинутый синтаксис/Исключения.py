#1.
def check_example(string):
    try:
        d = 0
        expression = string.split()
        for i in range(len(expression)):
            if expression[i] == '/':
                d = i
        expression.pop(d)
        for i in range(len(expression)):
            if expression[i].count('.') == 1: #таким образом переводим числа с плавующей точки как нужно нам без потери всего
                expression[i] = float(expression[i])
            else:
                expression[i] = int(expression[i])
        if int(expression[0]) and int(expression[1]): # по ТЗ видно, что если два интовых числа делятся, то нужно без точки выводить, иначе - с точкой
            result = expression[0] // expression[1]
        else:
            result = expression[0] / expression[1]
        return result
    except ZeroDivisionError:
        return ('ERROR')


print(check_example(input()))


#2.
def password(*args):
    D = dict()
    a = []
    d = 0
    for i in args:
        try:
            d = i
            a.append(int(i, 16))
            D[i] = f'Да, такой пароль имеет место быть, он даже имеет значение: {int(i, 16)}, в нашей 10 СС'
        except ValueError:
            a.append(d)
            D[d] = 'Братан, ты что-то попутал явно, такой пароль не мог быть в 16 СС записан, потому его нельзя перевести в 10 СС'
    wrapper_result = D.items()
    List_result_all_checks = list(wrapper_result)
    return List_result_all_checks


print(password('32h', '23a', '32a', '32d', '32g'))

# 3. способ 1
def decorator_of_control_1(func):
    def output(*args, **kwargs):
        result1 = func(*args, **kwargs)
        who_to_look_for = result1[2]
        result1_ol = result1[0]
        name_1_ol = result1[1][1]
        for i, x in result1_ol:
            if i == who_to_look_for:
                print('Спасибо, что поучаствовали в олимпиаде: Пробная Вышка! Ваши результаты:')
                return f'Название олимпиады: [{name_1_ol}]; статус: winner; результат: {x}'
        print('Спасибо, что поучаствовали в олимпиаде: [Пробная Вышка]! Ваши результаты:')
        return f'Название олимпиады:[{name_1_ol}]: Бро, тебя тут нет,но не расстраивайся, ты - призер'

    return output
def decorator_of_control_2(func):
    def output(*args, **kwargs):
        result2 = func(*args,**kwargs)
        who_to_look_for = result2[2]
        result2_ol = result2[0]
        name_2_ol = result2[1][1]
        for i in range(len(result2_ol)):
            if result2_ol[i][0] == who_to_look_for:
                temp = result2_ol[i][1]
                try:
                    print('Теперь переходим к олимпиаде: [Горные воробьи]')
                    print('Введите номер задачи, результаты которой хотите просмотреть в своей работе.')
                    task_of_check = input()
                    index = int(task_of_check) - 1
                    result_this_person_for_task = temp[index]
                    return f'Название олимпиады: [{name_2_ol}]; статус: winner; результаты за выполнение {task_of_check} задачи: {result_this_person_for_task}'
                except ValueError:
                    return f'{who_to_look_for}, вы ввели некорректное значение, введенное вами выражение должно быть числовым, то есть содержать лишь в себе число, составленное из цифр десятичной СС, попробуйте ещё раз'
                except IndexError:
                    return f'Название олимпиады: [{name_2_ol}]; статус: winner; результаты за {task_of_check} задачу ещё не выложены на сайт, если считаете, что произошла ошибка, обратитесь в техподдержку за уточнением информации'
                finally:
                    print(f'Спасибо, что поучаствовали в олимпиаде: [{name_2_ol}]! Ваши результаты:')
        return f'Название олимпиады: [{name_2_ol}]; Бро, тебя нет в победителях, но не расстраивайся, ты - призер'

    return output

@decorator_of_control_1
def olympiada1(q):
    format1 = olympiad1 = {"name": "Пробная вышка",
                           "winners": {
                               "Олеся Олимпиадникова": 594,
                               "Олег Олимпиадников": 587,
                               "Онисим Олимпиадников": 581,
                           }
                           }
    d = list(format1.items())
    name_olympiad_1 = d[0]
    d.pop(0)
    dictyonary_of_winners = d[0][1]
    list_of_winners = list(dictyonary_of_winners.items())
    return list_of_winners, name_olympiad_1, q

@decorator_of_control_2
def olympiada2(q):
    format2 = olympiad2 = {"name": "Горные воробьи",
             "winners": {
                 "Ольга Олимпиадникова": (20, 20, 19, 20),
                 "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                 "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
             }
             }
    d = list(format2.items())
    name_olympiad_2 = d[0]
    d.pop(0)
    dictyonary_of_winners = d[0][1]
    list_of_winners = list(dictyonary_of_winners.items())
    return list_of_winners, name_olympiad_2, q
print('Здравствуйте! Введите, сколько различных людей вы бы хотели проверить по результатам двух олимпиад')
skolko_chelovek_budem_proveryat_v_dvyx_olympyadax = int(input())
print('Сначала вы будете искать себя в системе первой олимпиады в нашем реестре: Пробная Вышка; Далее вторая олимпиада - Горные воробьи')
for _ in range(skolko_chelovek_budem_proveryat_v_dvyx_olympyadax):
    print('Введите Имя и Фамилию человека, которого собираетесь искать в наших двух олимпиадах:')
    d = input()
    print(olympiada1(d))
    print(olympiada2(d))

# 3. способ 2
format1 = olympiad1 = {"name": "Пробная вышка",
                       "winners": {
                           "Олеся Олимпиадникова": 594,
                           "Олег Олимпиадников": 587,
                           "Онисим Олимпиадников": 581,
                       }
                       }

format2 = olympiad2 = {"name": "Горные воробьи",
                       "winners": {
                           "Ольга Олимпиадникова": (20, 20, 19, 20),
                           "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                           "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
                       }
                       }


def check_result(name):
    name_olympyada1 = format1['name']
    name_olympyada2 = format2['name']
    try:
        points1 = format1["winners"][name]
        print(f'Название олимпиады:{name_olympyada1}; статус: winner; результат: {points1}')
    except KeyError:
        print(f'Название олимпиады:{name_olympyada1}; статус: призер')
    finally:
        print('-'*20)
    try:
        points_task_5_2 = format2['winners'][name][4]
        print(f'Название олимпиады:{name_olympyada2}; статус: winner; результат за 5 задачу: {points_task_5_2}')
    except IndexError:
        print(f'Название олимпиады:{name_olympyada2}; статус: winner ; резульатов за 5 задачу ещё нет')
    finally:
        print('-' * 20)


check_result('Ольга Олимпиадникова')
check_result('Олеся Олимпиадникова')


# 4.
def f():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print('AHAHAHHA, нет уж, ты попався навсегда сюда')
        f()
f()

#5.
# 5.
class LizardInCup(Exception):
    pass


class BarBurntDown(Exception):
    pass


def orderBeer():
    try:
        mugs = input("\nВы заходите в бар. \
        Сколько кружек лимонада заказываете?\n").lower()
        if mugs == "ящерица в стакане":
            raise LizardInCup
        if mugs == "где туалет?":
            raise BarBurntDown
        mugs = int(mugs)
        assert mugs < 2, "Кризис. Не больше одной кружки в одни руки."
        if mugs <= 0 or mugs >= 100:
            raise ValueError
    except AssertionError:
        print("Кризис. Не больше одной кружки в одни руки.")
    except ValueError:
        print("Вы не можете заказать такое число кружек, \
    держите одну кружку.")
    except LizardInCup:
        print("У нас закончились ящерицы. Приходите завтра!")
    except BarBurntDown:
        print("Поздравляем! Бар сгорел. Вы вышли из симуляции.")
    finally:
        print("Приходите ещё!")
    orderBeer()


orderBeer()



