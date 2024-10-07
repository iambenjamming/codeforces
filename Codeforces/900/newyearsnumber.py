t = int(input())

for _ in range(t):

    n = int(input())

    allowance = n // 2020

    if n % 2020 > allowance:
        print('NO')
    else:
        print('YES')