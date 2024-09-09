n = int(input())

ans = []

for i in range(n):
    if i&1:
        ans.append('I love')
    else:
        ans.append('I hate')

print(' that '.join(ans) + ' it')