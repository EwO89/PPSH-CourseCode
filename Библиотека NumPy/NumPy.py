

## Задача 1


import numpy as np

arr = np.array([[4, 2, 7],
                [9, 5, 1],
                [3, 8, 6]])

max_values = np.amax(arr, axis=0)

print(max_values)


## Задача 2


import numpy as np

arr = np.array([[8, 7, 9],
                [6, 8, 7],
                [9, 9, 8],
                [7, 6, 8]])

average_grades = np.mean(arr, axis=1)

print(average_grades)


### Задача 3

import numpy as np

arr = np.array([[10, 15, 20],
                [5, 25, 15],
                [30, 10, 5]])

total_sales = np.sum(arr, axis=1)

print(total_sales)


## Задача 4


import numpy as np

arr = np.array([1, 3, 2, 4, 2, 3, 1, 4, 4, 4, 5, 2])

unique_values, counts = np.unique(arr, return_counts=True)
max_count_index = np.argmax(counts)
most_frequent_value = unique_values[max_count_index]

print(f"Наиболее часто встречающееся значение: {most_frequent_value}")

## Задача 5


import numpy as np

array = np.array([[5, 4, 3], [2, 1, 1], [3, 3, 3]])

lowest_point = np.min(array)

count = np.count_nonzero(array == lowest_point)

print("Самая низкая точка на ландшафте:", lowest_point)
print("Количество вхождений:", count)


## Задача 6


import numpy as np

arr = np.array([[2, 7, 6],
                [9, 5, 1],
                [4, 3, 8]])

n = len(arr)
target_sum = n * (n**2 + 1) // 2

row_sums = np.sum(arr, axis=1)
rows_check = np.all(row_sums == target_sum)

column_sums = np.sum(arr, axis=0)
columns_check = np.all(column_sums == target_sum)

main_diagonal_sum = np.trace(arr)
main_diagonal_check = main_diagonal_sum == target_sum

secondary_diagonal_sum = np.trace(np.flip(arr, axis=1))
secondary_diagonal_check = secondary_diagonal_sum == target_sum

if rows_check and columns_check and main_diagonal_check and secondary_diagonal_check:
    print("Массив является магическим квадратом")
else:
    print("Массив не является магическим квадратом")

