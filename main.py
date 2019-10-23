print('Hello, \nWorld!')

#
a = 1
b = 2
c = a + b
print(c)

#
a = 56
print(a%10)

#
a = 56
b = 78
print(a > b)

#
a = 56
b = 78
print(a, b)

#
userName = 'Petr'
print('Name:', userName)

#
a = 10
b = 20
c = 0
print(a < b and b > c)

#
a = 10

b = 20
c = 0
print(a < b and b < c or not c)

#a = input()
#print(a)

#a = input()
#print(type(a))
#
# a = input('enter y name: ')
# print(a)

'''
test
'''

try:

x = int(input('Введите первое число:'))
y = int(input('Введите второе число:'))
z = int(input('Введите предполагаемый ответ: '))
otvet = x * y

if otvet == z:
    print('Верно!')
elif otvet !=  z:
    print('Ответ не верный, правильный ответ:' + str(otvet))

import this
##
from math import pi, sqrt
print(sqrt(pi))
#################################################################################
from math import pi, sqrt
# print(sqrt(pi))
## Просим ввести числа у пользователя
a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c: '))

##вычисляем дискриминант
d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / 2 * a
    x2 = (-b - sqrt(d)) / 2 * a
    print('x1=', str(x1), 'x2=', str(x2))
elif d == 0:
    x = -b / 2 * a
    print('x=', x)
# elif d < 0:
else:
    print('Действительных корней нет')
#################################################################################
a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
res = 0
# x = 1

while a <= b:
    if a % 2 != 0:
        res += a ##
    a += 1
print(res)
#################################################################################
a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
res = 0

if a % 2 == 0:
    a += 1

while a <= b:
    res += a
    a += 2
print(res)
#################################################################################
for i in 'hello world':
    print (i, end = '')
#################################################################################
a = 1
b = 5
res = 0
for i in range(a, b+1):
    if i % 2 != 0:
        res += i

print(res)
#################################################################################
pA = 10
pB = 5
pC = 2

summ = 100
count = 30

for a in range(int(summ / pA)):
    for b in range(int(summ / pB)):
        for c in range(int(summ / pC)):
            if (pA * a + pB * b + pC * c == summ) and a + b + c == count:
                print(a, ',', b, ',', c)
#################################################################################
S = 'Hello'
print(S[0] + S[1] + S[2] + S[3])
print (S[-len(S)])
#################################################################################
s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print (i, s[i])
#################################################################################
s = 'abcdefghijklm'
print(type(s))
#################################################################################
s = 'Python'
i = 0

while i < len(s):
    print(s[i], end=' ')
    i+=1

print(

for j in s:
    print(j, end=' ')
print()

)
#################################################################################
s = 'Python'
i = 0

while i < len(s):
    print(s[i], end=' ')
    i += 1

print()
for j in s:
    print(j, end=' ')
print()

stroka = 'Hello'

for symbol in stroka:
    if symbol in stroka:
        if symbol == 'y':
            break

#################################################################################
import re

res = re.findall('\d','05 Analytics Vidnya 28')
res1 = re.findall('\d+','05 Analytics Vidnya 28')
print(res)
print(res1)

#################################################################################
import re

res = re.split('W', 'Hello World')
print(res)

#################################################################################
import re
f = str(input('Введите фразу:'))
f1 = f.replace(' ', '')

i = 0
while i < (len(f1) // 2):
    if f1[i] != f1[-1-i]:
        print('-')
        break
    i += 1
else:
    print('+')
# for i in range(i, cnt-1):

#################################################################################
s = 'abc cde def'
res = ''
for i in s:
    if res.find(i) == -1 and i != ' ':
        res += i
print(res)
#################################################################################
f = input('Введите последовательность букв латинского алфавита нижним и верхним регистром:')
k = 0
j = 0
for i in f:
    if 'a' <= i <= 'z':
        k += 1
    if 'A' <= i <= 'Z':
        j += 1
print('lower:' + str(k), 'upper:' + str(j))

#################################################################################
s = 'dfgmdflkbmh09_'

for i in range(len(s)):
    if not ('a' <= s[0] <= 'z' or s[0] == '_'):
        print('no')
        quit()

    if not (('a' <= s[i].lower() <= 'z') or ('0' <= s[i] <= '9') or (s[i] == '_')):
        print('no')
        quit()
print('yes')

#################################################################################
import random

se = random.randint(1, 5)

print(se)
#################################################################################
# def printToConsole()
#     print('Hello World')
#
# printToConsole()

def dellSpace(s):
    res = ''

    for i in s:
        if i != ' ':
            res += i
    return res


s = 'Hello World'
print(dellSpace(s))


def addAndDiff(x, y):
    return x+y, x-y
print(addAndDiff(5,9))
#################################################################################
import temp

typp = input('Введите К, П, или Т').lower()

if typp == 'к':
    print(temp.sqr_circle())
elif typp == 'п':
    print(temp.sqr_pr())
elif typp == 'т':
    print(temp.sqr_triangle())
else:
    print('Error')

# 2d part

import math

def sqr_circle():
    r = float(input('Введите радиус:'))
    pl = math.pi * (r ** 2)
    return pl


def sqr_pr():
    a = float(input('Введите сторону a:'))
    b = float(input('Введите сторону b:'))

    pl = a * b
    return pl


def sqr_triangle():

    a = float(input('Введите сторону a:'))
    b = float(input('Введите сторону b:'))
    c = float(input('Введите сторону c:'))

    p = (a + b + c) /2
    pl = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return pl

#################################################################################
x = int(input('Введите число:'))
print(len(str(abs(x))))
#################################################################################
s = [12, 12.22, '12', [1, 3, 4]]
print(type(s[0]))
#################################################################################
s = 'Hello world'
print(list(s))
#################################################################################
from random import randint

n = randint(10, 15)
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

num = 0

for i in range(1, len(arr)):
    if abs(arr[i]) < abs(arr[num]):
        num = i
print(num + 1)
#################################################################################
from random import randint

n = 10
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

res = 0
j = 0

while j < len(arr):
    if arr[j] < 0:
        del(arr[j])
    else:
        j += 1
print(arr)
#################################################################################
from random import randint

n = 5
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

min_x = 0
max_x = 0
res = 0

for i in range(1, len(arr)):
    if arr[i] < arr[min_x]:
        min_x = i
print(arr[min_x])

for j in range(1, len(arr)):
    if arr[i] > arr[max_x]:
        max_x = j
print(arr[max_x])

if max_x < min:
    max_x, min_x = min_x, max_x

for k in range(min_x + 1, max_x):
    res += arr[k]

print(res)
#################################################################################
from random import randint

n = 5
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

min_x = 0
max_x = 0
res = 0

for i in range(1, len(arr)):
    if arr[i] < arr[min_x]:
        min_x = i
print(arr[min_x])

for j in range(1, len(arr)):
    if arr[i] > arr[max_x]:
        max_x = j
print(arr[max_x])

if max_x < min:
    max_x, min_x = min_x, max_x

for k in range(min_x + 1, max_x):
    res += arr[k]

print(res)
#################################################################################
from random import randint

n = 10
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

res = 0
j = 0

while j < len(arr):
    if arr[j] < 0:
        del(arr[j])
    else:
        j += 1
print(arr)
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'a')
file.close()
print(file.closed)
print(file.mode)
print(file.name)
#################################################################################file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

data = file.read()

file.close()

print(data)
print (len(data))

#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

data = file.readlines()
# data = file.readline()

file.close()

print(data)
print (len(data))
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

for line in file:
    print(line, end = '')

file.close()
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

while True:
    data = file.readline()
    print(data, end = '')

    if not data:
        break
file.close()
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

while True:
    data = file.read(2)
    print(data)

    if not data:
        break
file.close()
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

data = file.read(4)
print(data)
print(file.tell())

data = file.read(2)
print(data)
print(file.tell())

file.close()

#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'rb')

data = file.read(2)
print(data)
# print(file.tell())
file.seek(1, 2)

data = file.read(2)
print(data)

file.close()
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'a')

data = 'qwerty\n', 'qwerty2\n'

file.writelines(data)

file.close()
#################################################################################
with open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r') as file_handler:
    for line in file_handler:
        print(line, end='')

print('File Closed:' + ' ' + str(file_handler.closed))
#################################################################################
file = open(r'C:\Users\ihor.ivchenko\PycharmProjects\python_courses\file_1.txt', 'r')

# rus = ''
# eng = ''

N = file.readline()

d = {}

for line in file:
    # print(line, end = '')
    words = line.strip().split('-')
    ru = words[0].strip()
    en = words[1].strip().split(',')
    # print(words)
    # print(ru)
    # print(en)

    for en_word in en:
        d[en_word.strip()] = ru
file.close()

file_output = open('file_output.txt', 'w')
file_output.write(str(len(d)) + '\n')

for key in sorted(d):
    file_output.write(key + ' - ' + d[key] + '\n')

print(d)
#################################################################################
def readMass(path):
    file = open(path)
    N = 0
    mass = []
    for line in file:
        row = line.strip().split('  ')
        mass.append(row)
        N += 1
    file.close()
    return mass, N


def printMass(mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            print('%4s'%mass[i][j], end='')
        print()


mass, N = readMass('file_2.txt')
printMass(mass)

def change (mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if i == j:
                mass[i][j], mass[i][len(mass)-1-j] = mass[i][len(mass)-1-j], mass[i][j]
    return mass

res = change(mass)

print()

printMass(res)
#################################################################################
def fun1(a):
    x = a * 3

    def fun2(b):
        # nonlocal x
        return b + x

    return fun2


test_fun = fun1(4)

print(test_fun(7))
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################


