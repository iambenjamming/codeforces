t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    color = ''

    if a[0] != a[-1]:
        a[1] = -1 * a[1]
        for n in a:
            if n < 0:
                color += 'B'
            else:
                color += 'R'
        print('YES')
        print(color)
    else:
        print('NO')
