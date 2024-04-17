#1.
#answer - 4 1   5 6

#2.
#answer - П П Ш

#3.
#answer - bee

# 4.
#answer - True, False


# 5.
#answer - 1 4 16


# 6.
a = (x ** 2 for x in range(1, 6))
print(next(a))
next(a)
print(next(a))
next(a)
print(next(a))
#answer - 1 9 25

# 7.
cards = ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"] * 4
type = ['Бубна', "Черви", "Пики", "Крести"]
deck_of_cards = (card + ' ' + type[start // (len(cards) // 4)] for start, card in enumerate(
    cards))  # старт - второй аргумент enumeratete, который двигается +1 каждый перебор списка карт, *начало с 0 автоматически
k = 1
for card in deck_of_cards:
    if k < 9:
        print(card, end=' ')
        k += 1
    elif k == 9:
        k = 1
        print(card, end=' ')
        print()
print('Stop iteration')
#answer - таблица
