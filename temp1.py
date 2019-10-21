from random import randint

n = 5
arr = []
for i in range(n):
    arr.append(randint(-100, 100))

print(arr)

min_x = 0
max_x = 0
res = 0

for i in range(1, len(arr)):
    if arr[i] < arr[min_x]:
        min_x = i
print(arr[min_x])

for j in range(1, len(arr)):
    if arr[i] > arr[max_x]:
        max_x = j
print(arr[max_x])

if max_x < min:
    max_x, min_x = min_x, max_x

for k in range(min_x + 1, max_x):
    res += arr[k]

print(res)