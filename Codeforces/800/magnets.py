n =  int(input())

ans = 0
previous = ''

for _ in range(n):

    e = input()

    if e != previous:
        ans += 1

    previous = e
    
print(ans)