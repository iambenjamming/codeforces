import sys
 
t = int(sys.stdin.readline())
 
for _ in range(t):
 
    n = int(sys.stdin.readline())
 
    strengths = list(map(int, sys.stdin.readline().split()))
 
    if n == 1:
        print('1')
        continue
 
    groups = 0
 
    bit = strengths[0]
    
    for i in range(n):
        bit &= strengths[i]
        if bit == 0:
            groups += 1
            if i+1 < n:
                bit = strengths[i+1]
            else:
                bit = 0
    groups = max(1, groups)
            
    print(groups)