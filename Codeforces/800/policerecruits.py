n = int(input())
a = list(map(int, input().split()))

police = 0
crimes = 0

for e in a:
    if e == -1:
        if police > 0:
            police -= 1
        else:
            crimes += 1
    if e > 0:
        police += e

print(crimes)