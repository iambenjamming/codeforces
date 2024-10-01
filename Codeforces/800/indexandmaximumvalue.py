t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    high = max(map(int, input().split()))
    ans = []
    
    for _ in range(m):
        temp = input().split()
        operation = temp[0]
        l = int(temp[1])
        r = int(temp[2])
        
        if l <= high <= r:
            if operation == '+':
                high += 1
            else:
                high -= 1

        ans.append(high)
        
    print(*ans)