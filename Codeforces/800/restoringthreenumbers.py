a = list(map(int, input().split()))
a.sort()

ans = []

for i in range(3):
    ans.append(a[-1]-a[i])

print(*ans)