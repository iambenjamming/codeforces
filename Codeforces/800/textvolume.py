n = int(input())

s = list(input().split())

ans = 0

for w in s:
    count = 0
    for c in w:
        if c.isupper():
            count += 1

    ans = max(count, ans)

print(ans)