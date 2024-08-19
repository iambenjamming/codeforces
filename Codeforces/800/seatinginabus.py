t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    left = right = a[0]
    valid = True
    
    for i in range(1, n):
        if a[i] < left - 1 or a[i] > right + 1:
            valid = False
            break
        left = min(left, a[i])
        right = max(right, a[i])
    
    print('YES' if valid else 'NO')
