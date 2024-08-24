from collections import Counter

t = int(input())

for _ in range(t):

    n = int(input())

    a = list(map(int, input().split()))

    hashbrown = dict(Counter(a))

    orgbrown = list(sorted(hashbrown.items(), key = lambda x: -x[1]))

    ans = n - orgbrown[0][1]

    print(ans)
