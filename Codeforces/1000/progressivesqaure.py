from collections import Counter

t = int(input())

for _ in range(t):

    n, c, d = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    temp = [[0] * n for _ in range(n)]

    temp[0][0] = a[0]

    for i in range(1, n):
        temp[i][0] += temp[i-1][0] + c

    for i in range(n):
        for j in range(1, n):
            temp[i][j] += temp[i][j-1] + d

    real = [e for p in temp for e in p]

    compare1 = Counter(a)
    compare2 = Counter(real)

    if compare1 == compare2:
        print('YES')
    else:
        print('NO')
