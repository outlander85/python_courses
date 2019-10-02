import re
s1 = ''
s = input(str())
i = 0

s1 = re.findall('\w', s)
    if s1[0] == '_' or 'a' <= s1[0] <= 'z':
        while i <= len(s) - 1:
            if s1[i] == '_' or 'a' <= s1[i] <= 'z' or 'A' <= s1[0] <= 'Z' or '0' <= s1[0] <= '9':
                i += 1
            print('yes')
            else:
                print('no')
