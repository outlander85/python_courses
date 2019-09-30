a = int(input('Ввод количества строк:'))
x = 1
y = a
z = 0
while z <= a:
    print(' ' * y + ' ' + '^' * x)
    y -= 1
    x += 2
    z += 1