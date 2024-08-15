import math

t = int(input())

for _ in range(t):

    x , y = map(int, input().split())

    screens = 0

    screens += math.ceil(y/2)
    remain = (screens * (15)) - (y*4)
    
    if remain >= x:
        print(screens)
    else:
        needed = x - remain
        screens += max(1, math.ceil(needed/15))

        print(screens)
