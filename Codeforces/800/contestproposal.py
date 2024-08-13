t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    p1 = 0
    p2 = 0
    ans = 0

    while (p2 < n):

        if a[p1] > b[p2]:
            ans += 1
            p2 += 1
        else:
            p1 += 1
            p2 += 1

    print(ans)