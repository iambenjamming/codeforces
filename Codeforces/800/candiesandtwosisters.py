t = int(input())

for _ in range(t):
    n = int(input())

    if n&1:
        print(n//2)
    else:
        print(n//2 -1)
    