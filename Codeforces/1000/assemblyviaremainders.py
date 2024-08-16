t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    ans = [10000]
    count = 0

    for i in range(n-1):
        ans.append(ans[-1] +(count + a[i]))

    print(*ans)
