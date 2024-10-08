n, m = map(int, input().split())

if n < m:
    print('-1')
else:
    minsteps = n//2 + n%2

    if minsteps % m == 0:
        print(minsteps)
    else:
        minsteps += m-minsteps%m
        print(minsteps)

