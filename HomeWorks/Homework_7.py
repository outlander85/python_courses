#####################################################################################################
# FIRST TASK
#####################################################################################################
name = 0
surname = 1
cclass = 2
DOB = 3
day = 0
month = 1
year = 2
users = []


def readDB(path):
    users = []
    for line in open(path):
        tUser = []
        for i in line.split(' '):
            tUser.append(i.split('=')[1])
        users.append(tUser)
    return users


def printDB(dbName):
    for users in dbName:
        print('name=%-12s surname=%-12s class=%-5s birthday=%-10s' % (
            users[name], users[surname], users[cclass], users[DOB]), end='')


def older(arg1, arg2):
    if (int(arg1[2]) < int(arg2[2])):
        return True
    elif (int(arg1[2]) == int(arg2[2]) and int(arg1[1]) < int(arg2[1])):
        return True
    elif (int(arg1[2]) == int(arg2[2]) and int(arg1[1]) == int(arg2[1]) and int(arg1[0]) < int(arg2[0])):
        return True

    return False


def getIOlder(dbName):
    iOlderUser = 0
    for i in range(1, len(dbName)):
        date = dbName[i][DOB].split('.')
        dateOlder = dbName[iOlderUser][DOB].split('.')
        if older(date, dateOlder):
            iOlderUser = i
    return iOlderUser


def younger(arg1, arg2):
    if (int(arg1[2]) > int(arg2[2])):
        return True
    elif (int(arg1[2]) == int(arg2[2]) and int(arg1[1]) > int(arg2[1])):
        return True
    elif (int(arg1[2]) == int(arg2[2]) and int(arg1[1]) == int(arg2[1]) and int(arg1[0]) > int(arg2[0])):
        return True

    return False


def getIYounger(dbName):
    iYoungerUser = 0
    for i in range(1, len(dbName)):
        date = dbName[i][DOB].split('.')
        dateYounger = dbName[iYoungerUser][DOB].split('.')
        if younger(date, dateYounger):
            iYoungerUser = i
    return iYoungerUser


file = readDB('input.txt')
printDB(file)
print()
print('Самый старший:')
print(file[getIOlder(file)])
print()
print('Самый младший:')
print(file[getIYounger(file)])

#####################################################################################################
# SECOND TASK
#####################################################################################################

import math

sqr_circle = lambda r: math.pi * (r ** 2)


def sqr_pr(a, b):
    return a * b


def sqr_triangle(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


typp = input('Введите К, П, или Т').lower()

if typp == 'к':
    print(sqr_circle(float(input('Введите радиус:'))))
elif typp == 'п':
    print(sqr_pr(float(input('Введите сторону a:')), float(input('Введите сторону b:'))))
elif typp == 'т':
    print(sqr_triangle(float(input('Введите сторону a:')), float(input('Введите сторону b:')),
                       float(input('Введите сторону c:'))))
else:
    print('Error')
