#1.
x = int(input())
while (x % 2 == 1) or (str(x)[-1] != '5'):
    x = int(input())
#answer - (x % 2 == 1) or (str(x)[-1] != '5')

#2.
for i in range(10):
    print(i)
#answer i    10

# 3.
K = int(input())
N = int(input())
s = 0
while K <= N:
    if K % 2 == 1:
        s += K
    else:
        pass
    K += 1
print(s)

#4.
N = abs(int(input()))
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(factorial)
import math

print(math.factorial(10))
#anwer - 3628800
