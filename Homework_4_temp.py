def convert_to_binary(x):
    #x = int(input('Введите целое число в десятичной системе исчисления:'))  # Ввод числа
    res = ''  # результат, строка
    while x >= 1:
        res = str(x % 2) + res
        x = x // 2
    print(res)
