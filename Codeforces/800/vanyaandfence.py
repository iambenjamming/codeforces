n, h = map(int, input().split())

a = list(map(int, input().split()))

ans = 0

for p in a:
    if p > h:
        ans += 2
    else:
        ans += 1

print(ans)