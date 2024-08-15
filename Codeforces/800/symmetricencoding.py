t = int(input())

for _ in range(t):

    n = int(input())
    s = input()

    r = sorted(set(s))

    ans = []

    guide = {}

    i = 0
    j = len(r) - 1

    while(i < len(r)):
        guide[r[i]] = r[j]
        i += 1
        j -= 1

    for e in s:
        ans.append(guide[e])

    print(''.join(ans))
