t = int(input())

for _ in range(t):

    n = int(input())
    num = list(map(int, input().split()))

    diff = {}
    pair = 0

    for i in range(n):
        key = num[i] - i

        if key not in diff:
            diff[key] = 1
        elif key in diff:
            pair += diff[key]
            diff[key] += 1

    print(pair)
