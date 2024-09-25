t = int(input())
for _ in range(t):

    a,b,c,d = map(int, input().split())

    e = [a,b,c,d]
    e.sort()

    for i in range(len(e)):
        if e[i] == a:
            print(4-(i+1))
            break