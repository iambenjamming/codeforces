n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
b = [x for x in a if x+k <= 5]

print(len(b)//3)