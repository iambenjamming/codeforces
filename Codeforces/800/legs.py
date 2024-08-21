t = int(input())
 
for _ in range(t):
 
    n = int(input())
 
    print(n//4 + (1 if n%4 != 0 else 0))
