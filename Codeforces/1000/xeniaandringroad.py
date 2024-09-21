n, m = map(int, input().split())

tasks = list(map(int, input().split()))

ans = 0

cur = 1

for task in tasks:
    if task >= cur:
        ans += task - cur
    else:
        ans += task + (n-cur)
    cur = task

print(ans)