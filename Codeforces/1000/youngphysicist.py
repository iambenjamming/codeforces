from sys import stdin, stdout

n = int(stdin.readline())

xforce = []
yforce = []
zforce = []

while (n > 0):

    forces = input().split()
    forcex = int(forces[0])
    forcey = int(forces[1])
    forcez = int(forces[2])

    xforce.append(forcex)
    yforce.append(forcey)
    zforce.append(forcez)

    n -= 1

xsum = sum(xforce)
ysum = sum(yforce)
zsum = sum(zforce)

if xsum == 0 and ysum == 0 and zsum == 0:
    print("YES")
else:
    print("NO")
