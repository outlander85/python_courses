import math

class Circle:
    def __init__(self, r):
        self.r = r

    def getSquare(self):
        return math.pi * self.r**2


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getSquare(self):
        return self.a * self.b

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getSquare(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
