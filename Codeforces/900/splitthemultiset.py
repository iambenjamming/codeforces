t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    count = 0

    while n > 1:
        if n <= k:
            count += 1
            break
        else:
            n -= k - 1
            count += 1

    print(count)
