t = int(input())

for _ in range(t):
    n = int(input())

    c = n//5
    k = n%5
    vowels = 'aeiou'

    ans = ''

    for l in vowels:
        ans += l*c
        if k > 0:
            ans += l
            k -= 1

    print(ans)