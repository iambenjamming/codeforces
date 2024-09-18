k, r = map(int, input().split())

count = 1

while 1:
    temp = k * count
    if temp % 10 == 0 or temp % 10 == r:
        break
    else:
        count += 1

print(count)
