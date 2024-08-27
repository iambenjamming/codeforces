s = input()

ucount = 0
lcount = 0

for c in s:
    if c.isupper():
        ucount += 1
    else:
        lcount += 1

if ucount > lcount:
    print(s.upper())
else:
    print(s.lower())