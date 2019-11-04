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
            print('%4s' % mass[i][j], end='')
        print()


def printSumMass(mass):
    t = []
    for i in range(len(mass)):
        total = 0
        for j in range(len(mass)):
            total += int(mass[j][i])
            # print(total)
        t.append(total)

    return t


mass, N = readMass('file_hw_6_1.txt')
printMass(mass)
print('  --' * N)
# printSumMass(mass)
re = printSumMass(mass)
print(*re)


num = 1
for i in range(1, len(re)):
    if re[i] < re[num]:
        num = i
print(num)

####################################################################################

file = open(r'file_hw_6_2.txt')

N = file.readlines()
print(N)

for i in N:
    print(len(i))
    j = i.split(' ')
    print(len(j))
file.close()

