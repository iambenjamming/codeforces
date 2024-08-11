t = int(input())

for _ in range(t):

    s = input()

    if len(set(s)) > 1:
        ans = []

        for i in range(1, len(s)):
            ans.append(s[i])

        ans.append(s[0])
        print('YES')
        print(''.join(ans))
    else:
        print('NO')
            