t = int(input())

for _ in range(t):
    
    n, m, k = map(int, input().split())

    mnum = []
    knum = []

    for i in range(m):
        mnum.append(i+1)
    for i in reversed(range(m, n)):
        knum.append(i+1)

    gorilla = knum + mnum

    print(' '.join(map(str, gorilla)))
