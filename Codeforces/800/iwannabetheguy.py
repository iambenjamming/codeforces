n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

unique = set()

for i in range(1, max(len(x), len(y))):
    unique.add(x[min(i,x[0])])
    unique.add(y[min(i,y[0])])

if len(unique) < n:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")
