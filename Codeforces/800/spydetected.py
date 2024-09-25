t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = set(a)

    for e in b:
        temp = a.count(e)
        if temp == 1:
            print(a.index(e)+1)
            break