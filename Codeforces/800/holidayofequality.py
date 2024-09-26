n = int(input())
a = list(map(int, input().split()))

e = max(a)
ans = 0

for f in a:
    ans += abs(e-f)

print(ans)