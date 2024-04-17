#1.
print(sum([int(x ** 2) for x in range(1, 101)]))
#answer - 338350


#2.
#answer - [0 8 16 24 32]


# 3.
print(sum([x * x % 2 == 0 for x in range(1, 21)]))

# 4.
a = [int(input()) for x in range(10)]
print(sum([x * x % 2 == 0 for x in a[::2]]))
#answer - 3

#5.
print(sum([(x * x % 7 == 0 or x * x % 11 == 0) for x in range(1, 1001)]))
# answer - 220
