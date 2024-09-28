t = int(input())

for _ in range(t):

    n, m , q = map(int, input().split())

    teachers = list(map(int, input().split()))
    d = int(input())

    if d > max(teachers):
        print(n - max(teachers))
    elif d < min(teachers):
        print(min(teachers)-1)
    else:
        print((max(teachers)-min(teachers))//2)