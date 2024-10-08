t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())

    d1 = b-a
    d2 = b-c
    pmid = (a+c)/2

    if (pmid % b == 0 and pmid == int(pmid)) or ((d1+b) % c == 0 and d1+b > 0) or ((d2+b) % a == 0 and d2+b > 0):
        print('YES')
    else:
        print('NO')

