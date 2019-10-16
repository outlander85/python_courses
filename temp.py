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
