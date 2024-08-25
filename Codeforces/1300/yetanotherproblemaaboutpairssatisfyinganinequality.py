import bisect

t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    valid = [(j, i+1) for i, j in enumerate(a) if j < i+1]

    count = 0

    asubi = [x[0] for x in valid]
    index = [x[1] for x in valid]

    for e in asubi:
        count += bisect.bisect_left(index, e)
        
    print(count)
