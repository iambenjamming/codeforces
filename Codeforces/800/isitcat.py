t = int(input())

for _ in range(t):
    n = int(input())
    sound = input().lower()

    ref = 'meow'
    j = 0
    notcat = False

    i = 0
    while i < n and not notcat:
        if sound[i] == ref[j]:
            start = i
            while i < n and sound[i] == ref[j]:
                i += 1
            if start == i:
                notcat = True
            j += 1
            if j == 4:
                break
        else:
            notcat = True

    if notcat or j != 4 or i != n:
        print("NO")
    else:
        print("YES")

    

