n = int(input())

curpas = 0
bigpas = 0

for _ in range(n):

    a, b = map(int, input().split())

    curpas -= a
    curpas += b

    bigpas = max(bigpas, curpas)

print(bigpas)