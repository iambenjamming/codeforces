s = input()

n = len(s)
index = 0
found = False

for i in range(n//2 + 1, n):
    if s[:i] == s[n-i:]:
        index = i
        found = True
        break
    
if found:
    print('YES')
    print(s[:i])
else:
    print('NO')
