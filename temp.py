a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
res = 0

if a % 2 == 0:
    a += 1

while a <= b:
    res += a
    a += 2
print(res)