def isdvisible(v, i):
    return i % v == 0

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

ans = 0

for i in range(1, d+1):
    if isdvisible(k, i) or isdvisible(l, i) or isdvisible(m, i) or isdvisible(n, i):
        ans += 1

print(ans)