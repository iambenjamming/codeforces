def minim(n, k):
    total = n * (2*k + n - 1) // 2

    def difference(i):
        lefts = i * (2*k + i - 1) // 2
        rights = total - lefts
        return abs(lefts - rights)

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        diffmid = difference(mid)
        diffmid1 = difference(mid + 1)

        if diffmid <= diffmid1:
            right = mid
        else:
            left = mid + 1

    return difference(left)

t = int(input())

for _ in range(t):

    n, k = map(int, input().split())

    result = minim(n, k)

    print(result)
