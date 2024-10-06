t = int(input())
for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    e = a[:n-2]

    print(a[-1] - (a[-2]-sum(e)))