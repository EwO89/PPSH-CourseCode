#1.
surnames = ['Вотяк', 'Вотяков', 'Вотякович']
names = ['Александр', 'Алекс', 'Альберт']
patronymics = ['Романович']
for surname in surnames:
    for name in names:
        for patronymic in patronymics:
            print(f'Диплом с отличием вручается {surname}у {name}у {patronymic}у')
#answer - 9 строк

#2.
a = input()
b = int(input())
c = int(input())
print(f'{a}{b:>04}-{c:>03}')
#answer - all good


# 3.
a, b = int(input()), int(input())
for i in range(1):
    if len(str(a)) > len(str(b)):
        print(f"{a:>10}")
        print(f"{b:>10}")
        print(f"{a + b:>10}")
    elif len(str(a)) == len(str(b)):
        print(f"{a:>10}")
        print(f"{b:>10}")
        print(f"{a + b:>10}")
    elif len(str(a)) < len(str(b)):
        print(f"{b:>10}")
        print(f"{a:>10}")
        print(f"{a + b:>10}")
#answer - all good

# 4.
s = int(input())
r, k = abs(int(input())), abs(int(input()))
summa = s
for i in range(k):
    summa += summa / 100 * 1
print(f'{summa:,.2f}')
# answer - all good

# 5.
for a in range(1, 101):
    for b in range(1, 101):
        result = a * b
        if '0' in str(result):
            print(f'[DEBUG] {a=} {b=} {result=}')
#answer - all good

# 6. решение без формата
def return_ip(a, b, c, d):
    return f'{a:08b}.{b:08b}.{c:08b}.{d:08b}''\n'f'{a:b}.{b:b}.{c:b}.{d:b}''\n'f'{a:o}.{b:o}.{c:o}.{d:o}''\n'f'{a}.{b}.{c}.{d}''\n'f'{a:x}.{b:x}.{c:x}.{d:x}'


print(return_ip(127, 0, 0, 1))

# 6. решение c форматом
a, b, c, d = list(map(int, input().split()))

def return_ip(a, b, c, d):
    result = []
    for template in ['{:08b}', '{:b}', '{:o}', '{}', '{:x}']: #создали массив шаблон и перебрали его
        result.append('.'.join([template] * 4).format(a, b, c, d)) #метод формат применяется к объектам, то есть у нас аргументы формата это объекты, к которым применяем созданный ранее шаблон
    return '\n'.join(result) #жоин скрепляет элементы по переносу строки, в итоге все на разных строках


print(return_ip(a,b,c,d))
#answer - all good
