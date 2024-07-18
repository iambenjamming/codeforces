t = int(input())

for _ in range(t):

    x = int(input())

    ans = []

    while x:
            
        bit = x % 2
            
        if x & 2: 
            value = -1 if bit == 1 else 0
        else:
            value = bit
            
            
        ans.append(value)
            
        x = (x - ans[-1]) >> 1

    print(len(ans))
    print(*ans)
