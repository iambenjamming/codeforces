t = int(input())

for _ in range(t):

    n, a, b = map(int, input().split())

    ans = 0

    if 2*a > b:
        ans += n // 2 * b
        if n&1 == 1:
            ans += a
    else:
        ans += n * a

    print(ans)