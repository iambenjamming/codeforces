n = int(input())

names = {}

for _ in range(n):

    s = input()

    if s not in names:
        names[s] = 1
        print("OK")
        continue
    else:
        print(s + str(names[s]))
        names[s] += 1
        continue
