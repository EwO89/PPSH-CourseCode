# 1.
# answer - [2,2,2]

# 2.
# answer - [1,2,2]

# 3.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(sum(a) / n)
# answer - 4.2

# 4.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = int(input())
print(a[m])
# answer - a[m]

# 5.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for i in range(len(a)):
    if i % 2 == 0:
        s += a[i]
print(s)
# answer - 30
