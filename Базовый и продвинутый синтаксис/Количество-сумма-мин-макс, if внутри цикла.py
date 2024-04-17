# 1.
n = int(input())
a = []
for i in range(n + 1):
    a.append(i)
for i in range(len(a)):
    if a[i] % 3 == 0 and a[i] % 6 != 0:
        print(a[i])
# answer - 3,9,15


# 2.
n = int(input())
a = []
for i in range(10, n + 1):
    a.append(i)
for i in range(len(a)):
    if int(str(a[i])[-1]) % 2 == 0:
        print(a[i])
# answer - 10 , 12, 14, 16


# 3.
n = int(input())
a = []
for i in range(1, n + 1):
    a.append(i)
b = []
c = []
for i in range(len(a)):
    if n % 2 == 0 and a[i] % 2 == 0:
        b.append(a[i])
    elif n % 2 != 0 and a[i] % 2 != 0:
        c.append(a[i])
print(len(b))
print(sum(c))
# answer - 50/2500


# 4.
n = int(input())
if n % 3 == 0:
    k = 0
    m = int(input())
    a = [x for x in range(1, n + 1)]
    for i in range(len(a)):
        if a[i] % m == 0:
            k += 1
    print(k)
else:
    a = [n ** x for x in range(1, n + 1)]
    for i in range(len(a)):
        print(a[i], end=' ')
# answer - 8 64 512 4096 32768 262144 2097152 16777216
# answer - 14


# 5.
a, b, n = int(input()), int(input()), int(input())
h = []
for i in range(n):
    h.append(int(input()))
k = 0
for i in range(len(h)):
    if a ** 2 + b ** 2 == h[i] ** 2:
        if (h[i] > 10) and (h[i] % 3 == 0 or h[i] % 4 == 0):
            k += 1
print(k)
# answer = 1
