# 1.
def sum_numbers(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_numbers(10, 20, 30, 40))
print(sum_numbers(1, 2, 3))

# 2.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


print_kwargs(name=' Alice', age= 25, country=' USA')

# 3. первое решение
def filter_by_length(min_length, *strings):
    strings_new = []
    for string in strings:
        if len(string) >= min_length:
            strings_new.append(string)
    return strings_new


strings = ["hello", "world", "how", "are", "you"]

print(filter_by_length(len(min(strings, key=len)), *strings)) #второй аргумент в функции мин - ключ , по которому перебор ведем, в данном случае по длине строки в списке, но возвращает по итогу слово, а не длину,
#поэтому сверху ещё взял длину от строки


# 3. второе решение
def filter_by_length(min_length, *args):
    return [string for string in args if len(string) >= min_length]


strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(len(min(strings, key=len)), *strings))





# 4.
def calculate_total_price(cost, **kwargs):
    s = cost
    discount = 0
    for x, y in kwargs.items():
        discount += y
    return s - (s * (discount / 100))


print(calculate_total_price(100, student=10, coupon=20))
print(calculate_total_price(200, holiday=25))
print(calculate_total_price(500))


# 5.
def custom_print(*args, **kwargs):
    separator = kwargs.get('sep', ' ') #второй аргумент гет - что вернет (значение), если ключ не найден
    end_char = kwargs.get('end', '\n')
    if end_char != "\n":
        end_char += "\n"
    output = []
    for arg in args:
        output.append(str(arg))
    for key, value in kwargs.items():
        if key not in ['sep', 'end']:
            output.append(f'{key}={value}')
    print(separator.join(output), end=end_char)


custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
custom_print('Hello', 'World', sep=' ')
custom_print('apple', 'banana', 'cherry', sep=', ')
custom_print(a=1, b=2, end='...')

