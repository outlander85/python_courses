file = open(r'file_hw_6_2.txt')

N = file.readlines()
print(N)

for i in N:
    print(len(i))
    j = i.split(' ')
    print(len(j))
file.close()
