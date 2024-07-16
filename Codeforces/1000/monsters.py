t = int(input())
 
for _ in range(t):
    n, k = map(int, input().split())
    health = list(map(int, input().split()))
 
    answer = []
    excess = []
 
    for i in range(n):
        mod = health[i] % k
        if mod == 0:
            answer.append(i + 1)
        else:
            excess.append((mod, i + 1))
 
    excess.sort(reverse=True, key=lambda x: x[0])
 
    for mod, index in excess:
        answer.append(index)
 
    print(' '.join(map(str, answer)))
