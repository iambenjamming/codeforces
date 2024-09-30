t = int(input())

for _ in range(t):

    l, r = map(int, input().split())
    count = 0

    while l <= r:
        if l&1 and l+2 <= r:
            count += 1
            l += 2

        l += 1
    print(count)