t = int(input())

for _ in range(t):

    s = input()

    count = 0
    ans = 0

    for c in s:
        if c == '1':
            count += 1
        elif count:
            ans += (count + 1)

    print(ans)
