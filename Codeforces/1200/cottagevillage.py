n, t = map(int, input().split())

a = []

for _ in range(n):
    house = tuple(map(int, input().split()))
    a.append(house)

neighborhood = sorted(a, key = lambda x: x[0])
ideal = n * 2

for i in range(1, len(neighborhood)):
    temp = float(neighborhood[i][0] - neighborhood[i-1][0] - (neighborhood[i-1][1]/2 + neighborhood[i][1]/2))

    if float(t) > temp:
        ideal -= 2
    elif float(t) == temp:
        ideal -= 1
        
print(ideal)
