t = int(input())

for _ in range(t):

    l, r = map(int, input().split())

    count = 0
    diff = 0

    while l+diff <= r:
        count += 1
        l += diff
        diff += 1

    print(count)