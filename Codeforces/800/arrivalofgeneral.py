import bisect

n = int(input())
a = list(map(int, input().split()))

big= a.index(max(a))

a.reverse()

small = a.index(min(a))

if big > n-small-1:
    print(big+small-1)
else:
    print(big+small)