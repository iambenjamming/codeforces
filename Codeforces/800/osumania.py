t = int(input())

for _ in range(t):

    n = int(input())

    ans = []

    for _ in range(n):

        a = input()

        for i in range(4):
            if a[i] == '#':
                ans.insert(0, i+1)

    print(*ans)