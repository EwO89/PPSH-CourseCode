#пример работы кастомного декоратора с числом Фибоначчи
def my_cacher(func):
    D = dict()

    def output_func(x):
        if x not in D:
            D[x] = func(x)
        return D[x]

    return output_func


@my_cacher
def f(x):

    if x <= 1:
        return 1
    else:
        return f(x - 1) + f(x - 2)


for n in range(100):
    print(n, f(n))
    
   
  # 1.
import time


def timer(func):
    def time_for_work(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        fin = time.time()
        print(f'Функция {func.__name__} поработала ровно {fin - st} секунд')
        return result

    return time_for_work


@timer
def f(n, b):
    k = 0
    s = 0
    for x in range(n):
        for y in range(n):
            if (x + y) % 100 == 0:
                k += 1

    for x in range(b):
        s += x

    return k, s


print(f(int(input()), int(input())))



# 2.
n = int(input())


def cache(func):
    D = dict()

    def output(x):
        if x not in D:
            D[x] = func(x)
        return D[x]

    return output

@cache
def f(x):
    if x == 0:
        return 0
    else:
        return (f(x - 1) + 2) * 2


for i in range(n):
    print(i, f(i))

# 3.
from functools import reduce


def custom_decorator_logging(func):
    def output(*args, **kwargs):
        with open(name, 'a') as f:
            d = func(*args, **kwargs)
            f.write(f'Вызов функции {func.__name__} c аргументами {args} , {kwargs}\n')
        return d

    return output


name = 'opana.txt'


@custom_decorator_logging
def g(*args, **kwargs):
    a = []
    for las in args:
        a.append(las ** 2)
    a = reduce(lambda x, y: x * y, a)
    return a


print(g(40, 32, 32), g(5, 10))

# 4. будем решать задачу для случая, когда функция главная ВЕРНУЛА NONE
import time


def retry(max_attempts, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                attempts += 1
                time.sleep(delay)
            return None

        return wrapper

    return decorator


@retry(4, delay=3)
def some_function():
    return None


result = some_function()
print(result)


