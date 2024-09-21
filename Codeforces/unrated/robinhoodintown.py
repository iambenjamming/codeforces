import math

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1 or n == 2:
        print('-1')
        continue

    total = sum(p)
    average = total/n
    index = math.ceil(n//2)
    coin = 0

    p.sort()

    left = 0
    right = 10 ** 18

    while left < right:
        mid = (left + right)//2
        if p[index] >= (total + mid) / (2 * n):
            left = mid + 1
        else:
            right = mid

    print(right)
    
    
