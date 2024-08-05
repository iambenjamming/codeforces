t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    curdif = 0
    diflist = []
    found = False

    for i, juice in enumerate(a):
        if i+1 & 1 == 1:
            curdif += juice
            if curdif not in diflist and curdif != 0:
                diflist.append(curdif)
            elif curdif in diflist or curdif == 0:
                found = True
                break
        else:
            curdif -= juice
            if curdif not in diflist and curdif != 0:
                diflist.append(curdif)
            elif curdif in diflist or curdif == 0:
                found = True
                break

    if found:
        print('yEs')
    else:
        print('nO')
