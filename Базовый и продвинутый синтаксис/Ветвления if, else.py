# 1.
# answer - True

# 2.
login = input()
password = input()
if password == input():
    print('True')
else:
    print('False')
# answer - False

# 3. method number 1
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and a < c and a < d:
    print(a)
if b < a and b < c and b < d:
    print(b)
if c < b and c < a and c < d:
    print(c)
if d < a and d < c and d < b:
    print(d)

# 3. method number 2
a = [int(input()) for x in range(4)]
minim = 10000000000000000
for i in range(4):
    if a[i] < minim:
        minim = a[i]
print(minim)

# 3. method number 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min(a, b, c, d))

# 3. method number 4
print(min([int(input()) for x in range(4)]))
# answer - 5

# 4.
print(max([int(input()) for x in range(4)]))
# answer - 30

# 5.
a = int(input())
b = int(input())
c = int(input())
if (a + b > c) and (a + c > b) and (c + b > a):
    print('True')
else:
    print('False')
# answer - True

# 6.
a = int(input())
b = int(input())
c = int(input())
if (a + b == c) or (a + c == b) or (b + c == a):
    print('Вырожденный')
elif (a != b) and (a != c) and (c != b):
    print('Разносторонний')
if (a == b) and (a == c) and (c == b):
    print('Равносторонний')
if (a == b) or (b == c) or (a == c):
    print('Равнобедренный')
# answer - вырожденный
# к сожалению, не удалось без елифа обойтись, любой треугольник можно назвать разносторонним, у которого все три стороны разные, но так как используются ифы, то программа будет проверять вхождение всех ифов,
# то есть на позицию вырожденного, со всеми тремя сторонами разными, теоретически может попасться вариант, что треугольник разносторонний, но это не правда, ведь вырожденный треугольник - на самом деле
# отрезок, все три вершины которого находятся на нем. То есть логично поставить комбинацию иф вырожденный >> елиф для разностороннего, чтобы не было неоднозначности, если треугольник вырожденный, то в первую очередь
# проверяем это, если да - то к плану б) не переходим, тогда это отрезок, а иначе если треугольник разносторонний. Для других случаев иф корректен, ведь однозначность будет соблюдаться.

# 7.
a = [int(input()) for x in range(2)]
b = [int(input()) for y in range(2)]
c, d = abs(a[0] - a[1]), abs(b[0] - b[1])
v, n = [x + min(a[0], a[1]) for x in range(c + 1)], [y + min(b[0], b[1]) for y in range(d + 1)]
ans = []
for i in range(len(v)):
    if v[i] in n:
        ans.append(v[i])
ans = set(ans)
print(len(ans))
# answer - 7
# решил побаловаться, ифами елифами делать не очень удобно, но наглядно, оставлю вот так лучше :)





