t = int(input())

for _ in range(t):

    n = int(input())
    permutation = list(map(int, input().split()))

    l = 0
    r = n - 1

    min = 1
    max = n

    while l <= r:

        if permutation[l] == min:
            l += 1
            min += 1
        elif permutation[r] == max:
            r -= 1
            max -= 1
        elif permutation[l] == max:
            l += 1
            max -= 1
        elif permutation[r] == min:
            r -= 1
            min += 1
        else:
            break

    if l < r:
        print(l+1, r+1)
    else:
        print('-1')
