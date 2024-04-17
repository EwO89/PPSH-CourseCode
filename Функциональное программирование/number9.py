def compose_functions(functions):
    def composed_function(arg, index=0):
        if index >= len(functions):
            return arg
        new_arg = functions[index](arg)
        return composed_function(new_arg, index + 1)

    return composed_function


v = compose_functions([lambda x: x ** i for i in range(int(input())+1)])
print(v(2))
#Эта программа будет возводить все числа в ту степень, в которую мы попросим при пользовательском вводе. Например, если мы даём 4 функции всего, то все возводим в 4 степень в результате
#композиций функциий. Почему так происходит? Потому что программа берет последнюю i, которая создавала лист из функций анонимных, ведь итератор принял последнее значение 4. А дальше
#программа просто возводит постоянно новое значение в степень 4, пока все функции не закончат свою работу в листе.