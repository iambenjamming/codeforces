import math

t = int(input())

for _ in range(t):

    x, y, k = map(int, input().split())

    ref = max(x,y)

    if math.ceil(y/k) >= math.ceil(x/k):
        print((math.ceil(ref/k)*2))
    else:
        print((math.ceil(ref/k)*2)-1)
