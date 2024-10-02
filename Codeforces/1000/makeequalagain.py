t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    s = a[0]
    e = a[-1]

    if s == e:
        count = n
        for num in a:
            if num == s:
                count -= 1
            else:
                break
        for i in range(n-1, -1, -1):
            if a[i] == e:
                count -= 1
            else:
                break
        print(max(0, count))
    else:
        left = 0
        right = n-1
        countl = n
        countr = n
        while left < n and right >= 0:
            if s == a[left]:
                countl -= 1
                left += 1
            if e == a[right]:
                countr -= 1
                right -= 1
            if s != a[left] and e != a[right]:
                break
                
        print(min(countl, countr))

