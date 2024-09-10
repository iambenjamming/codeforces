n = int(input())

s = input().lower()

count = set()

for c in s:
    count.add(c)

if len(count) < 26:
    print('NO')
else:
    print('YES')