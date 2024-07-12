from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())

    health = list(map(int, stdin.readline().split()))

    target = 1
    count  = 0

    health.sort()

    for i in health:
        if i == target:
            target += 1
        elif i > target:
            minus = i - target
            count += minus
            target += 1

    print(count)
