n = int(input())

a = list(map(int, input().split()))

points = [0] * 1000000

bestcase = 0
previous = 0

for num in a:
    points[num-1] += num

for point in points:
    temp = max(bestcase, previous + point)
    previous = bestcase
    bestcase = temp

print(bestcase)
