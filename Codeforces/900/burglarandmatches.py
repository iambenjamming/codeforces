n, m = map(int, input().split())

containers = []

for _ in range(m):
    a, b = map(int, input().split())

    containers.append((a, b))

arranged = list(sorted(containers, key = lambda x: -x[1]))

bag = 0

for box, matches in arranged:
    if box <= n:
        bag += box*matches
        n -= box
    else:
        while(n > 0 and box > 0):
            bag += matches
            box -=1
            n -= 1
    if n < 0:
        bag -= matches
        break

print(bag)
