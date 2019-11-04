g = int(input('Введите количество гривен (от 0 до 999):'))
c = int(input('Введите количество копеек (от 0 до 99):'))
komma = ','

if g > 999 or g < 0 or c > 99 or c < 0:
    print('Вы ввели недопустимое число')
else:
    if 4 < g % 10 < 10 or g % 10 == 0 or 4 < g < 21:
        if 4 < c % 10 < 10 or c % 10 == 0 or 4 < c < 21:
            pr_c = (str(c) + ' копеек')
        elif c % 10 == 1:
            pr_c = (str(c) + ' копейка')
        elif 1 < c % 10 < 5:
            pr_c = (str(c) + ' копейки')
        if c == 0:
            print(str(g), ' гривен')
        elif g == 0:
            print(pr_c)
        else:
            print(str(g), ' гривен', komma, pr_c)
    elif g % 10 == 1:
        if 4 < c % 10 < 10 or c % 10 == 0 or 4 < c < 21:
            pr_c = (str(c) + ' копеек')
        elif c % 10 == 1:
            pr_c = (str(c) + ' копейка')
        elif 1 < c % 10 < 5:
            pr_c = (str(c) + ' копейки')
        if c == 0:
            print(str(g), ' гривна')
        elif g == 0:
            print(pr_c)
        else:
            print(str(g), ' гривна', komma, pr_c)
    elif 1 < g % 10 < 5:
        if 4 < c % 10 < 10 or c % 10 == 0 or 4 < c < 21:
            pr_c = (str(c) + ' копеек')
        elif c % 10 == 1:
            pr_c = (str(c) + ' копейка')
        elif 1 < c % 10 < 5:
            pr_c = (str(c) + ' копейки')
        if c == 0:
            print(str(g), ' гривны')
        elif g == 0:
            print(pr_c)
        else:
            print(str(g), ' гривны', komma, pr_c)
