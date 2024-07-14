t = int(input())

for _ in range(t):

    a, b, n = [x for x in map(int, input().split())]

    items = list(map(int, input().split()))
    
    timecount = 0

    if a == 1:
        print('1')
        continue

    for item in items:
        timecount += min(item, a-1)

    print(timecount+b)
