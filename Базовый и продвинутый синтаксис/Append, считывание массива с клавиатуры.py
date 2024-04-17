#1.
n = int(input())
m = int(input())
a = []
a.append(n)
a.append(m)
print(a, sum(a))
#anwer - [12, 34] 46

#2.
p = input()
a = p.split()
b = []
for i in range(len(a)):
    b.append(a[i])
print(b[0],b[-1])
#answer - Программирование школы


#3.
p = input()
a = p.split()
maxim = -100000
b = []
for i in range(len(a)):
    if len(a[i]) > maxim:
        maxim = len(a[i])
        if len(b) == 0:
            b.append(a[i])
        else:
            b.pop(0)
            b.append(a[i])
print(b)
#answer - нетипичный

# 4.
n = int(input())
a = []
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i)
print(sum(a))
#answer - 234168

#5.
p = input()
a = p.split()
b = set(a)
c = list(b.copy())
maxim = 0
slovo_4asto = ''
for i in range(len(c)):
    if a.count(c[i]) > maxim:
        maxim = a.count(c[i])
        slovo_4asto = c[i]
print(slovo_4asto, maxim)
#answer - cat 6
