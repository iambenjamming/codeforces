n = int(input())

height = list(map(int, input().split()))

towers = {c: height.count(c) for c in set(height)}
sorted_towers = dict(sorted(towers.items(), key=lambda item: item[1], reverse=True))

print(list(sorted_towers.values())[0], len(set(height)))
