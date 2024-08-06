t = int(input())

for _ in range(t):
    n, s, m = map(int, input().split())

    intervals = []

    for _ in range(n):
        i1, i2 = map(int, input().split())

        temp = (i1, i2)
        intervals.append(temp)

    bestint = abs(0 - intervals[0][0])

    for i in range(1, len(intervals)):
        bestint = max(bestint, abs(intervals[i][0] - intervals[i-1][1]))

    bestint = max(bestint, abs(intervals[-1][1] - m))

    if bestint >= s:
        print('YES')
    else:
        print('NO')
