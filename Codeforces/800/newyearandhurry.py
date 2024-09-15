n, k = map(int, input().split())

time = 240 - k
ans = 0

for i in range(1, n+1):
    if time - (5*i) >= 0:
        time -= (5*i)
        ans += 1
    else:
        break

print(ans)
