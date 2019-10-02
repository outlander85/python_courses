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
#################################################################################
#################################################################################
#################################################################################
#################################################################################
