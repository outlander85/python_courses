import figures

figuresList = []


for i in range(3):
    choice = input.lower()("Круг(к), прямоугольник(п) или треугольник(т): ")

    if choice == 'к':
        figure = figures.Circle(float(input("Радиус: ")))


    elif choice == 'п':
        l = float(input("Длина: "))
        w = float(input("Ширина: "))

        figure = figures.Rectangle(w, l)

    elif choice == 'т':
        a = float(input("Первая сторона: "))
        b = float(input("Вторая сторона: "))
        c = float(input("Третья сторона: "))

        figure = figures.Triangle(a, b, c)

    figuresList.append(figure)

choice1 = input("Вывести площадь(пл), или периметр(пр)?")


maxS = 0
maxP = 0
name_p = ''
name_s = ''
for i in figuresList:
    s = i.getSquare()
    p = i.getPerimeter()

    if maxS < s:
        maxS = s
        name_s = i.name

    if maxP < p:
        maxP = p
        name_p = i.name


if choice1 == 'пл':
    print()
    print('Максимальная площадь у: ' + name_s + 'а - ' + str(maxS) + ' кв. сантиметров')
elif choice1 == 'пр':
    print()
    print('Максимальный периметр у: ' + name_p + 'а - ' + str(maxP) + ' сантиметров')
else:
    print('Error')
