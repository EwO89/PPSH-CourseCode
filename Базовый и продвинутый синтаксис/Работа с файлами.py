#1.
def return_line(name):
    with open(name, 'r') as f:
        data = f.read()
        return data


print(return_line('pick1.txt'))


# 2.
def return_first_string(name):
    with open(name, 'r') as f:
        first = f.readline()
        return first


print(return_first_string('pick2.txt'))


# 3.
def return_List_strings(name):
    with open(name, 'r') as f:
        List = f.readlines()
        return List


print(return_List_strings('pick3.txt'))

# 4.
def return_List_strings(name):
    with open(name, 'r') as f:
        List = f.read().split('\n')
        return List


print(return_List_strings('pick4.txt'))


# 5.
def string(name):
    with open(name, 'r') as f:
        for line in f:
            print(line, end='')


string('pick5.txt')

# 6.
def return_sting(name):
    with open(name, 'r') as f:
        List = f.read().split('\n')
        return ' '.join(List)


print(return_sting('pick6.txt'))

# 7.
def return_string(name):
    with open(name, 'r') as f:
        for line in f:
            print(line.rstrip('\n\t'))


return_string('pick7.txt')


# 8.
def sting(name):
    with open(name, 'r') as f:
        for line in f:
            print(line.rstrip('!?.\n'))


sting('pick8.txt')


# 9.
def write_str(name, string):
    with open(name, 'w') as f:
        f.write(string)


write_str('pick99.txt', 'more')


# 10.
def write_str(name, string):
    with open(name, 'w') as f:
        f.write(string + '\n')


write_str('pick10.txt', 'nosorog')

# 11. первый способ
def list_write(name, List):
    with open(name, 'w') as f:
        for line in List:
            if line != List[-1]:
                f.write(line + '\n')
            else:
                f.write(line)


list_write('pick11.txt', ['Dog', 'Wolf', 'Cat'])


# 11. второй способ (как в решении, немного странный, потому что это непрезентабельно выглядит
def list_write(name, List):
    with open(name, 'w') as f:
        f.writelines(List)


list_write('pick11.txt', ['Dog', 'Wolf', 'Cat', 'Racoon'])

# 12. первый способ
def Andrey_string(name1, name2):
    with open(name1, 'r') as f1:
        with open(name2, 'w') as f2:
            s = f1.read()
            List_as_f1 = s.split('\n')
            for line in List_as_f1:
                if line != List_as_f1[-1]:
                    f2.write(line + '\n')
                else:
                    f2.write(line)


Andrey_string('pick12.txt', 'pick12copy.txt')

# 12. второй способ потупее, потому что лишний \n добавляется из-за принта
def Andrey_string(name1, name2):
    with open(name1, 'r') as f1:
        with open(name2, 'w') as f2:
            for line in f1:
                print(line, file=f2)


Andrey_string('pick12.txt', 'pick12copy.txt')


# 13.
def Andrey_string(name1, name2):
    with open(name1, 'r') as f:
        with open(name2, 'w') as g:
            for line in f:
                s = line.strip()
                if s.startswith('hello') and s.endswith('world'):
                    g.write(line)


Andrey_string('pick13.txt', 'pick13copy.txt')

# 14.
def dictyonary_reorginize(name):
    s = {}
    with open(name, 'r', encoding='utf-8') as f:
        musor = f.readline()
        data = f.readlines()
        for line in data:
            string = line.split()
            s[string[0]] = (string[1], string[2])
    return s


print(dictyonary_reorginize('pick14.txt'))
