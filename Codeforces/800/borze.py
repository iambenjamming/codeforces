s = input()

i = 0
ans = ''

while i < len(s):

    if s[i] == '-':
        i+=1
        if s[i] == '.':
            ans += '1'
        else:
            ans += '2'
    elif s[i] == '.':
        ans += '0'

    i += 1
print(ans)