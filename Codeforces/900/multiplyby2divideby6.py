def solve(n):

    count = 0

    while n > 0 and n != 1:

        if n % 6 == 0:
            count += 1
            n //= 6
        elif n % 3 != 0:
            return -1
        else:
            count += 1
            n *= 2
    return count

t = int(input())

for _ in range(t):

    n = int(input())

    print(solve(n))
