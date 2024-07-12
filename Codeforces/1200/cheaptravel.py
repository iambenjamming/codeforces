import sys

nmab = sys.stdin.readline().split()

n = int(nmab[0]) #required rides
m = int(nmab[1]) #rides per m ticket
a = int(nmab[2]) #cost for 1 ride
b = int(nmab[3]) #cost per m ticket

spent = 0

if n < m:
    if b < a or n > 1:
        spent += b
        n -= n
        print(spent)
        sys.exit()
    elif a < b and n == 1:
        spent += a
        n -= n
        print(spent)
        sys.exit()

while (n > 0):

    if float(b/m) < float(a):
        if n >= m:
            used = (n // m) * b
            spent += used
            n -= n // m * m
        elif n < m:
            if b < a:
                spent += b
                n -= n
            elif b > a:
                used = a
                spent += used
                n -= 1
            elif b == a:
                spent += a
                n -= n
        elif m > n:
            used = b
            spent += used
            n -= m
        elif b == a:
            used = n * a
            spent += used
            n -= n
    elif float(b/m) > float(a):
        used = n * a
        spent += used
        n -= n
    elif float(b/m) == float(a):
        used = n * a
        spent += used
        n -= n

print(int(spent))
