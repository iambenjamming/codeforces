t = int(input())

for _ in range(t):

    n, k = [int(x) for x in input().split(' ')]

    casserole = list(map(int, input().split()))

    casserole.sort()

    actions = 0

    for slices in range(0, k - 1):
        if casserole[slices] > 1:
            cutnum = casserole[slices] - 1
            actions += cutnum

    actions += n - casserole[-1]

    print(actions)
