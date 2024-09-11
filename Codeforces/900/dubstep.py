s = input().split('WUB')

while '' in s:
    s.remove('')

print(' '.join(s))