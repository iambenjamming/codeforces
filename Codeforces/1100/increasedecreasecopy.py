t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    copy = float('inf')
    i = 0
    j = 0
    ans = 0

    while(i < n):
        ans += abs(a[i] - b[j])

        if a[i] <= b[-1] <= b[j] or b[j] <= b[-1] <= a[i]:
            copy = 0
        else:
            copy = min(copy, min(abs(a[i] - b[-1]), abs(b[j] - b[-1])))
            
        i += 1
        j += 1

    ans += copy + 1

    print(ans)
