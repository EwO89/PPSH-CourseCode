#1.
n = int(input())
a = [int(input()) for x in range(n)]
c = a.copy()


def return_dict(q):
    b = dict(zip(a, c))
    return b
print(return_dict(n))
#answer - {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5}


# 2.
n = int(input())
a = [int(input()) for x in range(1, n + 1)]
s = []
for i in range(len(a)):
    s.append(a[i] * a[i])


def generation_print(q):
    b = dict(zip(a, s)) #создаем на основе двух список словарь, где элементы массива а - ключи, а s - значения соответственно
    return b


print(generation_print(n))
#answer - {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#3.
def return_in_list(n):
    dictionary = {input(): int(input()) for x in range(n)}
    listok = list(dictionary.items()) #превращаем словарь в список, состоящий из кортежей элементов словаря (ключ-значение)
    s = 1
    for i in range(len(listok)):
        s *= listok[i][1]
    return s


print(return_in_list(4))
#answer - -165209625

# 4.
alf = '.,:;!?'
s = input()
k = 0
for i in range(len(s)): 
    if s[i] in alf:
        k += 1
print(k)
#answer - 12

# 5.
def f(s):
    a = []
    digits = '0123456789'
    alf = 'abcdefghigklmnopqrstuwzxyz'
    k = 0
    for i in range(len(s)):
        if s[i] in alf:
            k += 1
        if k == 0:
            return 'NO'
        else:
            for y in range(len(s)):
                if s[y] in digits:
                    a.append(int(s[y]))
    a.sort(reverse=True)
    b = set(a)
    return list(b)


d = f(input())
for i in range(len(d)):
    print(d[i], end=' ')
#answer - 1 2 4 5 6 7 8 9




