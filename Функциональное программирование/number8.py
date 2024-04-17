from functools import reduce


def create_function_with_arguments(func, arguments):
    def new_func():
        return func(arguments)

    return new_func


def f(argumets):
    return reduce(lambda x, y: x * y, argumets)


v = create_function_with_arguments(f, [x for x in range(1, int(input()) + 1)])
print(v())
