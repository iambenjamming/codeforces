t = int(input())

for _ in range(t):

    n = list(map(int, input().split()))

    n.sort()

    if n[-1] == n[0] + n[1]:
        print('YES')
    else:
        print('NO')

