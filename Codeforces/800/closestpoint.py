t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    if n > 2:
        print('NO')
        continue
    else:

        if max(a) - 1 == min(a):
            print('NO')
            continue
        else:
            print('YES')