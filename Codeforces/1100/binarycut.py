t = int(input())

for _ in range(t):

    s = [i for i in input()]

    f = 0
    ans = 1

    for i in range(1, len(s)):

        if s[i] != s[i-1]:
            ans += 1

        if s[i] == '1' and s[i-1] == '0':
            f = 1

    print(ans-f)
