n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

ans = a[n-1] - a[0]

for i in range(n, m):
    ans = min(ans, a[i]-a[i-(n-1)])
    
print(ans)