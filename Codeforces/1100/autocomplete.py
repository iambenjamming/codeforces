s = input()
n = int(input())
first = input()

ans = first

if first[:len(s)] == s:
    found = True
else:
    found = False

for _ in range(n-1):
    e = input()

    if e[:len(s)] == s:
        if e < ans:
            ans = e
            found = True
if found:
    print(ans)
else:
    print(s)
