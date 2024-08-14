t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    s = 0
    for i in range(n):
        s += a[i]
        a[i] = (a[i], i)
        
    a.sort()
    ans = [0] * n
    ans[a[n - 1][1]] = n - 1
    
    for i in range(n - 1, 0, -1):
        s -= a[i][0]
        if s < a[i][0]:
            ans[a[i - 1][1]] = i - 1
        else:
            ans[a[i - 1][1]] = ans[a[i][1]]
    print(*ans)
