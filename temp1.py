s = 'dfgmdflkbmh09_'

for i in range(len(s)):
    if not ('a' <= s[0] <= 'z' or s[0] == '_'):
        print('no')
        quit()

    if not (('a' <= s[i].lower() <= 'z') or ('0' <= s[i] <= '9') or (s[i] == '_')):
        print('no')
        quit()
print('yes')
