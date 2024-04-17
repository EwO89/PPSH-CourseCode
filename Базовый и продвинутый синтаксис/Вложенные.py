#1.
print('Таблица умножения')
for i in range(1,11):
    print('')
    for x in range(1,11):
        print(i*x,end = ' ')
#answer - таблица умножения

# 2.
l = int(input())
r = int(input())
counter = 0
for x in range(l, r + 1):
    for y in range(l, r + 1):
        for k in range(l, r + 1):
            if x ** 2 + y ** 2 == k ** 2:
                counter += 1
print(counter)
#answer - 26

# 3.
def find_divisors(x):
    a = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            a.append(j)
            if j != x // j:
                a.append(x // j)
    a.sort()
    a.pop(-1)
    return sum(a)


n = int(input())
print('Ваши пары:')
for i in range(1, n):
    for x in range(i + 1, n):
        if i == find_divisors(x) and x == find_divisors(i):
            print(i, x)
#answer - 220 284


# 4.
n = int(input())
print('Ваши числа:')
for i in range(1000, 10000):
    a = [(int(x)) ** n for x in str(i)]
    if sum(a) == i:
        print(i, ',', end=' ')
# answer - 1634 , 8208 , 9474
