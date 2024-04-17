def filter_odd(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))


print(filter_odd([32, 30, 1, 2]))
