def partial_apply(func, x):
    def partial_func(y):
        return func(x, y)

    return partial_func


v = partial_apply(lambda x, y: x + y, 4)
print(v(5))
