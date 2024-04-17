# 1.
#answer - ['Женя', 'Вася']

# 2.


a = [int(input()) for x in range(5)]
c = lambda x: x ** 3
for i in range(len(a)):
    print(c(a[i]))
# answer - 2. [8, 64, 216, 512, 1000]

# 2. 2 способ


a = [int(input()) for x in range(5)]
print(list(map(lambda x: x ** 3, a)))
#answer - [8, 64, 216, 512, 1000]


# 3.
a = [int(input()) for x in range(7)]
print(list(filter(lambda x: x < 0, a)))
#answer - [-1, -7, -8, -10]


# 4.
from functools import reduce

a = [int(input()) for x in range(1, 9)]
a = reduce(lambda x, y: x * y, a)
print(a)
#answer - 40320

# 5. решение немного кривое под частный случай с целыми числами в массиве искомом


a = [(int(input())) ** 2 for x in range(12)]
print(int(max(list(filter(lambda x: x % 9 == 0, a))) ** 0.5))
# answer - 6

#5. решение получше
print(max(filter(lambda x: x ** 2 % 9 == 0, [2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2])))
