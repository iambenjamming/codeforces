n, a, b, c = map(int, input().split())

ans = 0
for i in range(4001):
    for j in range(4001):
        kc = n - (i*a + j*b)
        if kc < 0:
            break
        if kc/c == kc//c:
            ans = max(ans, i+j+(kc//c))

print(ans)