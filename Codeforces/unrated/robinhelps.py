t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    robin = 0
    pcount = 0

    for c in p:
        if c >= k:
            robin += c
        elif robin > 0 and c == 0:
            robin -= 1
            pcount += 1

    print(pcount)
