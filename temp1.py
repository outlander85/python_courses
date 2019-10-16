import temp

typp = input('Введите К, П, или Т').lower()

if typp == 'к':
    print(temp.sqr_circle())
elif typp == 'п':
    print(temp.sqr_pr())
elif typp == 'т':
    print(temp.sqr_triangle())
else:
    print('Error')