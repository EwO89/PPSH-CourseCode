#1.
#answer - 2

#2.
#answer - 3

# 3.
def is_even(n):
    if n % 2 == 0:
        print((n, " is even"))
    else:
        print((n, " is odd"))


is_even(4)
# answer - 3

# 4.
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# answer - n - 1

# 5.
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
print(is_palindrome('ШАЛАШ'))


# answer - - 1

# 6.
def multiplylist(lst):
    result = 0
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
    return result


print(multiplylist([31, 43, 30]))
# answer - исправление кода

