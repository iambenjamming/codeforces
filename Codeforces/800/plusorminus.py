t = int(input())
for _ in range(t):

    a,b,c = map(int, input().split())

    if c == max(a,b,c):
        print('+')
    else:
        print('-')