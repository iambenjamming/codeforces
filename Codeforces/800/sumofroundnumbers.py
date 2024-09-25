t = int(input())

for _ in range(t):
    n = int(input())
    ref = n

    ans = []

    if ref % 10**(len(str(n))-1) != 0:
        count = len(str(n))-1
        while ref % 10**(count) != 0:
            temp = int(str(ref%10**(count)))
            ans.append(ref - temp)
            ref -= (ref-temp)
            count -= 1
        while 0 in ans:
            ans.remove(0)

        if sum(ans) != n:
            ans.append(n-sum(ans))
        print(len(ans))
        print(*ans)
    else:
        print('1')
        print(n)
