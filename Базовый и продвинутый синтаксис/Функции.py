# 1.
def sum_from_numbers_list(n):
    a = [int(input()) for x in range(n)]
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


print(sum_from_numbers_list(8))
#answer - 77

# 2.
def number_range(n):
    if n in range(1, 10):
        return 'Yes'
    else:
        return 'No'


print(number_range(7))
# answer - YES

# 3.
def find_divisors(n):
    a = []
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            a.append(j)
            if j != n // j:
                a.append(n // j)
    a.sort()
    a.pop(-1)
    return sum(a)


def perfect_number(n):
    if n > 0:
        if n == find_divisors(n):
            return 'True'
        else:
            return 'False'
    else:
        return 'Оно даже не положительное для начала, чудик'


print(perfect_number(8128))
#answer - True

# 4.
def number_is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return 'True'
    else:
        return 'False'


print(number_is_palindrome(1234567899876554321))
#answer - False

# 5.
def number_is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


print(number_is_prime(123321))
#answer - False

# # 6.
n = abs(int(input()))


def number_is_Fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    return number_is_Fibonacci(n - 1) + number_is_Fibonacci(n - 2)


print(number_is_Fibonacci(n))
#answer - 34


