n = int(input())
visited = [False] * n
i = 0
k = 1

while True:
    if all(visited):
        print('YES')
        break
    
    if visited[i]:
        print('NO')
        break
    
    visited[i] = True
    i = (i + k) % n
    k += 1
