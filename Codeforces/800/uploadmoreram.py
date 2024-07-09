import math

t = int(input())

while (t > 0):

    nk = input().split()

    n = int(nk[0])
    k = int(nk[1])

    rate = float(1 / k)
    needed = n - 1
    timeneeded = int(round((needed / rate)) + 1)

    print(timeneeded)

    t -= 1
