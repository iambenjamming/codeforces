t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    evens = []
    bigodd = 0
    count = 0

    for e in a:
        if e&1:
            bigodd = max(bigodd, e)
        else:
            evens.append(e)

    if len(evens) == 0 or len(evens) == n:
        print(count)
        continue

    evens.sort()

    for f in evens:
        while(bigodd <= f):
            bigodd += max(evens)
            count += 1
        if bigodd > f:
            temp = f + bigodd
            bigodd = max(temp, bigodd)
            count += 1

    print(count)
