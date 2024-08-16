t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ref1 = a[0]

    leftover = []
    more = []

    for e in a:
        if e % ref1 != 0:
            leftover.append(e)

    if len(leftover) > 0:
        ref2 = leftover[0]

        for f in leftover:
            if f % ref2 != 0:
                more.append(f)

    if len(more) == 0:
        print('YES')
    else:
        print('NO')
