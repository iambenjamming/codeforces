t = int(input())

for _ in range(t):
    
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    aset = set(a)
    
    for _ in range(m):
        s = input()
        if len(s) != n:
            print('NO')
            continue
        
        hashbrown = {}
        used = set()
        valid = True
        
        for i, char in enumerate(s):
            if char in hashbrown:
                if hashbrown[char] != a[i]:
                    valid = False
                    break
            else:
                if a[i] in used:
                    valid = False
                    break
                hashbrown[char] = a[i]
                used.add(a[i])
        
        if valid and len(hashbrown) == len(aset):
            print('YES')
        else:
            print('NO')
