a = int(input('Ввод количества строк:'))
x = 1 ## Количество символов "^"
y = a ## Количество пробелов
z = 0 ## Количество строк
while z < a:
    print(' ' * y + ' ' + '^' * x)
    y -= 1
    x += 2
    z += 1