def getkey(dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None

t = int(input())

for _ in range(t):

    n = int(input())

    trace = list(map(int, input().split()))

    hashbrown = {}
    ans = []
    var1 = 0

    for num in trace:
        if num == 0:
            ans.append(chr(ord('a') + var1))
            hashbrown[chr(ord('a') + var1)] = 1
            var1 += 1
            continue
        ans.append(getkey(hashbrown, num))
        hashbrown[getkey(hashbrown, num)] += 1
        

    print(''.join(ans))
