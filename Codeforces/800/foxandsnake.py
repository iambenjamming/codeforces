n, m = map(int, input().split())

ans = []
count = 1

for i in range(n):
    if i%2 == 0:
        ans.append(('#'*m))
    else:
        if count&1:
            ans.append(('.'*(m-1))+'#')
            count += 1
        else:
            ans.append('#'+('.'*(m-1)))
            count += 1

for l in ans:
    print(l)