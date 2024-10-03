t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if k > n or k == 1:
        print(n)
    else:
        ans = 0
        while n:
            ans += (n % k)
            n //= k
        print(ans)
