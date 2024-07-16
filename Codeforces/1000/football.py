n = int(input())

record = []

for i in range(n):
    record.append(input())

team_counts = {}

for team in record:
    if team in team_counts:
        team_counts[team] += 1
    else:
        team_counts[team] = 1

max_count = 0
winner = None

for team, count in team_counts.items():
    if count > max_count:
        max_count = count
        winner = team

print(winner)
