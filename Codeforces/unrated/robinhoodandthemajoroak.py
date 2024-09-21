t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    odd = (n - (n-k)) // 2
    
    if n&1:
        odd = k - odd

    if odd % 2 == 0:
        print('YES')
    else:
        print('NO')
