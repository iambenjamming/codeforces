s = input()

valid = {'H','Q','9'}

flag = False

for c in s:
    if c in valid:
        flag = True

if flag:
    print('YES')
else:
    print('NO')