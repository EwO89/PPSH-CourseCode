from functools import reduce


def reduce_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)


print(reduce_sum([5, 4, 3]))
