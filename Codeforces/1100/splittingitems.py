t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    a.sort(reverse=True)
    
    for i in range(1, n, 2):
        if k == 0:
            break
        c = a[i-1] - a[i]
        if c <= k:
            a[i] = a[i-1]
            k -= c
        else:
            a[i] += k
            k = 0
 
    guo = 0
    b = 0

    for i in range(n):
        if i&1:
            b += a[i]
        else:
            guo += a[i]
    
    print(guo-b)
