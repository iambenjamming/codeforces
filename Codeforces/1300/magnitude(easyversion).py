t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    c = 0
    r = 0

    for n in nums:
        r += n
        c = max(abs(r), abs(c+n))

    print(c)
