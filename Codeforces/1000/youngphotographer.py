n, o = map(int, input().split())

ans = 0
record = []

for _ in range(n):
    num = list(map(int, input().split()))
    num.sort()

    cool = (num[0], num[1])
    record.append(cool)

    temp = 0
    
    if num[0] > o or o > num[1]:
        temp += min(abs(o-num[0]), abs(o-num[1]))

    ans = max(temp, ans)

for i in range(0, len(record)):
    for j in range(1, len(record)):
        if record[i][1] < record[j][0]:
            print('-1')
            exit()
        elif record[j][1] < record[i][0]:
            print('-1')
            exit()

print(ans)
