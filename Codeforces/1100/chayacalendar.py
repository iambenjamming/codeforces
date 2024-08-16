t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    
    now = 0
    for e in a:
        now = ((now + e) // e) * e
    
    print(now)

