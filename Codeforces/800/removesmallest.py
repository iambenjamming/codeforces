t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    if n == 1 or len(set(a)) == 1:
        print('YES')
        continue

    a.sort()

    flag = True

    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')