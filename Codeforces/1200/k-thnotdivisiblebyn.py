from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    nk = stdin.readline().split()
    n = int(nk[0])
    k = int(nk[1])

    if k < n:
        print(k)
    else:
        passednondiv = k // (n - 1)
        setofnondiv = (n - 1) * passednondiv
        pos = k - setofnondiv

        if pos == 0:
            kth = (n* passednondiv) - 1
            print(kth)
        else:
            kth = pos + (n * passednondiv)
            print(kth)
