t = int(input())

for _ in range(t):

    s = input()

    one = int(s[0]) + int(s[1]) + int(s[2])
    two = int(s[3]) + int(s[4]) + int(s[5])

    if one == two:
        print('YES')
    else:
        print('NO')