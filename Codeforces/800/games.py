n = int(input())

teams = []

for _ in range(n):
    a,b = map(int, input().split())
    teams.append((a,b))

count = 0

for i in range(len(teams)):
    for j in range(min(i+1, len(teams)), len(teams)):
        if teams[i][0] == teams[j][1]:
            count += 1
        if teams[i][1] == teams[j][0]:
            count += 1

print(count)
