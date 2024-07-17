s, n = [x for x in list(map(int, input().split()))]

dragons = []
die = False

for _ in range(n):
    x , y = [x for x in list(map(int, input().split()))]
    dragons.append((x, y))

dragons.sort()

for dragon in dragons:
    if s > dragon[0]:
        s += dragon[1]
    else:
        die = True
        break


if die == True:
    print("NO")
else:
    print("YES")


