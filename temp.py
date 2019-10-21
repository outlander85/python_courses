from random import randint

n = 10
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

res = 0
j = 0

while j < len(arr):
    if arr[j] < 0:
        del(arr[j])
    else:
        j += 1
print(arr)