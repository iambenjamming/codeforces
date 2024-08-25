t = int(input())

for _ in range(t):

    n = int(input())

    s = input()

    a = [i if c == 'L' else n-1-i for i, c in enumerate(s)]
    ans = []
    index = 0
        
    current = sum(a)
    
    gains = sorted([(max(i, n-1-i) - val, i) for i, val in enumerate(a)], reverse=True)

    for gain, eh in gains:
        if gain <= 0:
            break
        current += gain
        ans.append(current)
        
    ans.extend([current] * (n - len(ans)))
    print(*ans)
