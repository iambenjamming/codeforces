n = int(input())
num = input()

ans = []

if n&1 != 1:
    
    count = 0
    
    for n in num:
        if count&1 == 0 and count != 0:
            ans.append('-')
        ans.append(n)
        count += 1
else:

    count = 0
    
    for n in num:
        if count&1 == 0 and count != 0:
            ans.append('-')
        ans.append(n)
        count += 1

    ans.pop(-2)

print(''.join(ans))
