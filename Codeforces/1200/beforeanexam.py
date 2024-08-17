d, sumTime = map(int, input().split())

sumMin = 0
sumMax = 0
minTimes = []
maxTimes = []
ans = []

for _ in range(d):
    minTime, maxTime = map(int, input().split())
    minTimes.append(minTime)
    maxTimes.append(maxTime)
    sumMin += minTime
    sumMax += maxTime

if sumMin <= sumTime <= sumMax:
    remaining = sumTime - sumMin
    ans = minTimes.copy()
    
    for i in range(d):
        if remaining == 0:
            break
        additional = min(remaining, maxTimes[i] - minTimes[i])
        ans[i] += additional
        remaining -= additional
    
    if remaining == 0:
        print('YES')
        print(*ans)
    else:
        print('NO')
else:
    print('NO')
