t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))
    s = input()

    ans = 0
    L = 0
    R = s.count('R')

    for i in range(n):
        if s[i] == 'L':
            L += 1
        ans += a[i] * min(L, R)

        if s[i] == 'R':
            R -= 1
            
    print(ans)
        
