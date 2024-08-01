def guess(num):

    if num <= k:
        emojis = num * (num + 1) // 2
    elif num > k:
        emojis =(k + 1) * (k) // 2 + (k)*(k - 1) // 2 - (2 * k - 1 - num) * (2 * k - num) // 2

    return emojis

t = int(input())

for _ in range(t):

    k, x = map(int, input().split())

    emosum = k ** 2

    if emosum <= x:
        print(2*k-1)
    else:
        left = 0
        right = 2 * k - 1
        mid = left + (right - left) // 2

        while guess(mid) >= x or guess(mid+1) < x:
            if guess(mid) < x:
                left = mid
            else:
                right = mid
            mid = left + (right - left) // 2

        print(mid + 1)
