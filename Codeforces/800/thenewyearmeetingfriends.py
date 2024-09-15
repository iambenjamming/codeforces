a = list(map(int, input().split()))

a.sort()

ans = abs(a[0]-a[1])+abs(a[1]-a[2])

print(ans)