n = int(input())

a = list(map(int, input().split()))

small = a[0]
big = a[0]

count = 0

for i in range(1, n):
    if a[i] < small:
        count += 1
        small = a[i]
    elif a[i] > big:
        count += 1
        big = a[i]

print(count)