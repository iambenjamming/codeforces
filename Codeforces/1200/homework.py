s = input()
k = int(input())

if k >= len(s):
    print('0')
    print('')
else:

    hashmap = {}
    distinctcount = len(set(s))

    for c in s:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    hashbrown = dict(sorted(hashmap.items(), key = lambda x: x[1]))

    for key, value in hashbrown.items():
        if value - k > 0 or k <= 0:
            break
        elif value - k <= 0:
            k -= value
            hashbrown[key] = 0
        
    countgone = 0
    for key, value in hashbrown.items():
        if value == 0:
            countgone += 1
            while(key in s):
                s = s.replace(key, '')
    
    print(distinctcount-countgone)
    print(s)

    
