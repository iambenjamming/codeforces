t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    L, R = map(int, input().split())
    
    therange = max(0, min(r, R) - max(l, L) + 1)
    
    if l == L and r == R:
        ans = therange - 1
    elif l == L or r == R:
        ans = therange
    else:
        ans = therange + 1
    
    print(ans)
