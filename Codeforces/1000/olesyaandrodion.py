n, t = map(int, input().split())

if len(str(t)) > n:
    print('-1')
else:
    base = 10**(n-1)
    remainder = base % t
    answer = base + (t - remainder) % t
    print(answer)

