l = []
for i in range(1667):
    temp = str(i)
    if i % 3 == 0 or temp[-1] == '3':
        continue
    else:
        l.append(i)

t = int(input())

for _ in range(t):

    n = int(input())
    print(l[n-1])
