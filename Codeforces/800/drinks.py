n = int(input())
a = list(map(int, input().split()))

ans = sum(a) / n

print('%.12f' %ans)