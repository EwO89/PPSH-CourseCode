
def factorial(n):
    if n <= 0:
        return f'Ошибка. Наше число n должно быть положительное'
    else:
        if n == 1:
            return 1
        else:
            return factorial(n - 1) * n


print(factorial(int(input())))

#Второе решение этой же задачи можно посмотреть в 8 номере
