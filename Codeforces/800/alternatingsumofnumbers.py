t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        if i&1:
            ans -= a[i]
        else:
            ans += a[i]

    print(ans)