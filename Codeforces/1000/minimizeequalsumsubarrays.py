t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    ans = a[1:] + a[:1]

    print(*ans)