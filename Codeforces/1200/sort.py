t = int(input())

for _ in range(t):

    n, q = map(int, input().split())

    a = input()
    b = input()

    apre = [[0] * 26 for _ in range(n + 1)]
    bpre = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(26):
            apre[i + 1][j] = apre[i][j]
            bpre[i + 1][j] = bpre[i][j]
        apre[i + 1][ord(a[i]) - ord('a')] += 1
        bpre[i + 1][ord(b[i]) - ord('a')] += 1

    for _ in range(q):

        l, r = map(int, input().split())

        l -= 1

        count = 0
    
        for i in range(26):
            freakya = apre[r][i] - apre[l][i]
            freakyb = bpre[r][i] - bpre[l][i]
            count += abs(freakya - freakyb)

        print(count//2)
