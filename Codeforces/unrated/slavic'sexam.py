t = int(input())

for _ in range(t):
    s1 = input()
    ref = input()

    ans = []
        
    i = 0
    j = 0

    for c in s1:
        if j < len(ref) and (c == ref[j] or c == '?'):
            ans.append(ref[j])
            j += 1
        elif c == '?':
            ans.append('a')
        else:
            ans.append(c)

    if j == len(ref):
        print('YES')
        print(''.join(ans))
    else:
        print('NO')
