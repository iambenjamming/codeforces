t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    if n == 1:
        print(a[0])
        continue
    if n == 3:
        print(max(a[0], a[2]))
        continue

    ans = 0
    
    for i in range(n):
        if len(a[:i]) % 2 == 0 and len(a[i+1:]) % 2 == 0:
            ans = max(ans, a[i])

    print(ans)
