n = int(input())
stripe = list(map(int, input().split()))

stripe1 = 0
stripe2 = sum(stripe)
ans = 0

for i in range(len(stripe) - 1):
    stripe1 += stripe[i]
    stripe2 -= stripe[i]

    if stripe1 == stripe2:
        ans += 1

print(ans)