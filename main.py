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