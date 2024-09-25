n = int(input())
a = list(map(int, input().split()))

sereja = 0
dima = 0

left = 0
right = n-1

while left < right:

    if a[left] > a[right]:
        sereja += a[left]
        left += 1
    else:
        sereja += a[right]
        right -= 1

    if a[left] > a[right]:
        dima += a[left]
        left += 1
    else:
        dima += a[right]
        right -= 1

if n&1:
    sereja += sum(a) - (sereja+dima)

print(sereja, dima)
