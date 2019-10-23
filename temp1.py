def readMass(path):
    file = open(path)
    N = 0
    mass = []
    for line in file:
        row = line.strip().split('  ')
        mass.append(row)
        N += 1
    file.close()
    return mass, N


def printMass(mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            print('%4s'%mass[i][j], end='')
        print()


mass, N = readMass('file_2.txt')
printMass(mass)


def change (mass):
    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if i == j:
                mass[i][j], mass[i][len(mass)-1-j] = mass[i][len(mass)-1-j], mass[i][j]
    return mass

res = change(mass)

print()

printMass(res)



