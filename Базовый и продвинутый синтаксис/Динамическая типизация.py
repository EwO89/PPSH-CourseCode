#1.
#answer - 108

# 2.
import copy

a = [int(input()) for x in range(5)]
b = a[:]
c = a.copy()
z = copy.copy(a)
n = copy.deepcopy(a)
m = list(a)
print(b, c, z, n, m, sep=',')
print(sum(a))
#answer - 5 35

#3.
#answer -966


# 4. - первый способ - подлиннее
import sys

animals = [input() for x in range(8)]
animalss = animals.copy() #создал копию, чтобы потом сравнимать с искомым списком, эту же копию будем уменьшать, удаляя все элементы определенного уникального встреченного слова. То есть задумка в том, чтобы
n = [] #находить уникальные строчки, убирать с копии их все, совершать пересчёт удаленных элементов из копии, далее пересчитываем кол-во удаленных - это нам покажет, сколько таких строчек было в искомом списке.
index = [] #так как мы по порядку находили в искомом списке уникальные строчки, то и в список n, отвечающий за нахождение этих самых строк пополняется элементами в том же порядке. Список C создан для того, чтобы
c = [] #пополнять туда количество найденных животных по конкретному слову. Список индексов был задуман, чтобы потом обращаться в список с, отбирая количество по конкретному типу. То есть в массив с так же по порядку
for i in range(len(animals)): #все добавлялось, тогда первое число в списке, состоящем из списков - указатель на конкретный тип из списка С, так как порядок соблюден, то мы всегда попадаем с помощью указателя i
    c.append([] * len(animals)) #в нужный тип и далее берем к каждому типу нужное найденное количество животных для конкретного названия животного.
k = 0
for i in range(len(animals)):
    flag = False #когда ещё ничего не нашли, то флаг выключен, как находим уникальное что-то, то далее работаем с этим
    if animals[i] in animalss and flag == False:
        flag = True
        index.append([i, animals[i]])
        n.append(animals[i])
        x = []
        for q in range(len(animalss)):
            if animals[i] == animalss[q]:
                x.append(q)
        z = len(x)
        counter = 0
        for s in range(z): #математически можно догадаться, почему был заведён счетчик, почему при удалении из списка элемента мы всегда обращаемся далее в елифе в индекс s - counter (кратко - из-за сдвига к нулю всех эл.)
            if z == len(x):
                animalss.pop(x[s])
                x.pop(s)
                counter += 1
            elif z != len(x):
                animalss.pop(x[s - counter] - counter)
                x.pop(s - counter)
                counter += 1
        k = z
        c[i].append(k)
    elif animals[i] not in animalss and flag == True:
        flag = False
names_animals = n
count_this_animal = []
number_index = []
for i in range(len(index)):
    number_index.append(index[i][0])
for i in range(len(names_animals)):
    count_this_animal.append(c[number_index[i]][0])
dictyonary_animals = dict(zip(names_animals, count_this_animal))
summa_1 = 0
summa_2 = 0
for i in range(1, 4):
    summa_1 += sys.getrefcount(i)
for i in range(len(n)):
    summa_2 += sys.getrefcount(n[i])
print(summa_1, summa_2, sep=' , ')
print(animals)
print(dictyonary_animals)
# answer - 3000000446 , 20. В памяти всё осталось

# 4 - второй способ покороче
import sys

animals = [input() for x in range(8)]
dictyonary_animals = {}
for animal in animals:
    if animal not in dictyonary_animals:
        dictyonary_animals[animal] = 1
    else:
        dictyonary_animals[animal] += 1
summa_1, summa_2 = 0, 0
for i in range(1, 4):
    summa_1 += sys.getrefcount(i)
for i in range(len(animals)):
    summa_2 += sys.getrefcount(animals[i])
print(summa_1, summa_2, sep=' , ')
# answer - тут уже 3000000432 , 21

# 5.
backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara",
            2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7],
            [7, 7, 7]] + [[8, 8]] * 5
count_is = 0
count_equal = 0
for i in range(len(backpack)):
    for j in range(i + 1, len(backpack)):
        if backpack[i] is backpack[j]:
            count_is += 1
        if backpack[i] == backpack[j]:
            count_equal += 1
print(count_is, count_equal, sep=' , ')
#answer - 15 , 21

# 6.
import copy
a = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
a.append(a)
b = copy.deepcopy(a)
b[6].append('salt')
b[6].append('pepper')
print(a) #первая итерация
print(b[6][4], b[6][-1]) #вторая итерация с добавлениями

#answer - tomatoes pepper
