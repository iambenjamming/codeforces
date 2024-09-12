n = int(input())
a = list(map(int, input().split()))

ans = 0
count = 0

for i in range(1, n):
    if a[i] < a[i-1]:
        count = 0
    else:
        count += 1

    ans = max(ans, count)

print(ans+1)