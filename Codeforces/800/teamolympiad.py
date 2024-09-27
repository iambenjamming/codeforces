n = int(input())
c = input().split()

t = min(c.count('1'), min(c.count('2'), c.count('3')))

print(t)

indice_1 = []
indice_2 = []
indice_3 = []

for i in range(len(c)):
    if c[i] == '1':
        indice_1.append(i)
    elif c[i] == '2':
        indice_2.append(i)
    elif c[i] == '3':
        indice_3.append(i)

for _ in range(t):
    print(indice_1.pop()+1, indice_2.pop()+1, indice_3.pop()+1)