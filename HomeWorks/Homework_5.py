inn = -1

t1 = {'invnum': 1, 'name': 'Chair', 'cnt': 55, 'price': 1500}
t2 = {'invnum': 2, 'name': 'Table', 'cnt': 55, 'price': 1200}
t3 = {'invnum': 3, 'name': 'Laptop', 'cnt': 60, 'price': 9000}
t4 = {'invnum': 4, 'name': 'Server', 'cnt': 5, 'price': 120000}

c1 = t1['cnt']
c2 = t2['cnt']
c3 = t3['cnt']
c4 = t4['cnt']

print(t1['name'], str(t1['cnt'])+'pcs', str(t1['price'])+'$')
print(t2['name'], str(t2['cnt'])+'pcs', str(t2['price'])+'$')
print(t3['name'], str(t3['cnt'])+'pcs', str(t3['price'])+'$')
print(t4['name'], str(t4['cnt'])+'pcs', str(t4['price'])+'$')

while inn:
    inn = int(input('Enter invnum (1-4), (0 = write changes)'))
    if inn != 0:
        c = int(input('Enter new count:'))
        if inn == t1['invnum']:
            c1 = c
        elif inn == t2['invnum']:
            c2 = c
        elif inn == t3['invnum']:
            c3 = c
        else:
            c4 = c
t1['cnt'] = c1
t2['cnt'] = c2
t3['cnt'] = c3
t4['cnt'] = c4

print(t1['name'], str(t1['cnt'])+'pcs', str(t1['price'])+'$'
print(t2['name'], str(t2['cnt'])+'pcs', str(t2['price'])+'$')
print(t3['name'], str(t3['cnt'])+'pcs', str(t3['price'])+'$')
print(t4['name'], str(t4['cnt'])+'pcs', str(t4['price'])+'$')