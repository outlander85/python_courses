import temp

# choice = input('Круг(к), прямоугольник(п), или треугольник(т):')

fi

for i in range(3)

if choice == 'к':
    figure = temp.Circle(float(input('Радиус:')))
elif choice == 'п':
    l = float(input('Длина:'))
    w = float(input('Ширина:'))

    figure = temp.Rectangle(w, l)

elif choice == 'т':
    a = float(input('Первая сторона:'))
    b = float(input('Вторая сторона:'))
    c = float(input('Третья сторона:'))

    figure = temp.Triangle(a, b, c)

print(figure.getSquare())
