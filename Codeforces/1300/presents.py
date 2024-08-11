n, k = map(int, input().split())
 
a = list(map(int, input().split()))
temp = a[0]
a.pop(0)

latest = 0
count = 0

for x in a:
    count += ((x - latest - 1)// k) + 1
    latest = x

print(count + (n - latest) // k)
