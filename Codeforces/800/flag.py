n, m = map(int, input().split())

colors = []

for _ in range(n):
    c = input()

    temp = set()
    
    for b in c:
        temp.add(int(b))

    if len(temp) > 1:
        print('NO')
        exit()

    for a in temp:
        colors.append(a)
        
flag = True

for i in range(1, len(colors)):
    if colors[i-1] == colors[i]:
        flag = False

if flag:
    print('YES')
else:
    print('NO')