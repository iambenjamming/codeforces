from sys import stdin, stdout
 
t = int(stdin.readline())
 
for _ in range(t): # while (t--){}
 
    n, m, k = map(int, stdin.readline().split())
    khalf = k / 2

    a = set(i for i in map(int, stdin.readline().split()) if i <= k)
    
    b = set(i for i in map(int, stdin.readline().split()) if i <= k)
 
    required = set(range(1, k + 1))
    a_contribution = required & a
    b_contribution = required & b
    ab = a_contribution | b_contribution
 
    if len(a_contribution) + len(b_contribution) >= k and len(a_contribution) >= k / 2 and len(b_contribution) >= k / 2:
        if len(ab) >= k:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
