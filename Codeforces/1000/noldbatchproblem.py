n, k = map(int, input().split())

temp = []

for i in range(2, n+1):
        if all(i % j != 0 for j in temp):
            temp.append(i)

count = 0
for i in range(len(temp) - 1):
    if temp[i] + temp[i+1] + 1 in temp:
        count += 1

if count >= k:
    print('YES')
else:
    print('NO')
