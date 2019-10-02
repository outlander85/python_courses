s = 'one two three четырнадцать:)'
id = 0
s1 = s.split()
for i in range(1, len(s1)):
    if len(s1[id]) < len(s1[i]):
        id = i
print(s1[id])