s = input()
t = input()

flag = True

if len(s) != len(t):
    print('NO')
    exit()

for i in range(len(s)):
    if s[i] != t[-1 -i]:
        flag = False
        break

print('YES' if flag else 'NO')