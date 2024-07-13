import sys
import bisect
 
n = int(sys.stdin.readline())
shops = list(map(int, sys.stdin.readline().split()))
 
shops.sort()
 
t = int(sys.stdin.readline())
 
for _ in range(t):
 
    budget = int(sys.stdin.readline())
    
    index = bisect.bisect_right(shops, budget)
    print(index)