a = [int(x) for x in input()]
b = [int(x) for x in input()]

ans = []

for i in range(len(a)):
    ans.append(a[i]^b[i])

print(''.join(map(str, ans)))