t = int(input())

for _ in range(t):

    n = int(input())

    level1 = set()
    level2 = set()

    count = 0

    for _ in range(n):

        x, y = map(int, input().split())

        if y == 1:
            level2.add(x)
        else:
            level1.add(x)


    for f in level1:
        if f in level2:
            count += len(level1) + len(level2) - 2
        
    for e in level1:
        if e+1 in level2 and e+2 in level1:
            count += 1

    for g in level2:
        if g+1 in level1 and g+2 in level2:
            count += 1
    
    print(count)
