t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    if n == 2:
        print(min(a))
        continue
    else:

        medians = []

        for i in range(n-2):
            temp = a[i:i+3]
            temp.sort()

            medians.append(temp[1])

        ans = max(medians)

        print(ans)
