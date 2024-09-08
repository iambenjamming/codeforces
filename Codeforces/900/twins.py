n = int(input())

coins = list(map(int, input().split()))

total = sum(coins)

coins.sort()

eviltwin = 0
count = 0

while eviltwin <= total:
    eviltwin += coins[-1]
    total -= coins[-1]
    coins.pop()

    count += 1

print(count)