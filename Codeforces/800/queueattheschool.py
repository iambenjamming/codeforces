n, t = map(int, input().split())

line = input()

for _ in range(t):

    temp = ['B'] * n

    for i in range(n):
        if line[i] == 'G':
            if temp[max(i-1,0)] != 'G' and line[max(i-1,0)] != 'G':
                temp[max(i-1,0)] = 'G'
            else:
                temp[i] = 'G'

    line = temp
    
print(''.join(line))
