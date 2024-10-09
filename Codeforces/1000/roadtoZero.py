t = int(input())

for _ in range(t):

    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if 2*a < b:
        ans = a*(x+y)
        print(ans)
    else:

        spentb = b*min(x, y)
        remainder = max(x,y) - min(x,y)

        print(spentb + remainder*a)