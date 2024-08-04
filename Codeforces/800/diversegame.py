t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    if n == 1 and m == 1: e = input(); print('-1'); continue

    storage = []
    done = False

    for _ in range(n):

        s = list(map(int, input().split()))

        if m > 1:
            ans = []

            for j in range(1, len(s)):
                ans.append(s[j])
            ans.append(s[0])

            print(' '.join(map(str, ans)))
            done = True
        else:
            storage.append(s)

    if done == False:
        for i in range(1, len(storage)):
            temp = storage[i]
            print(''.join(map(str, temp)))
        temp = storage[0]
        print(''.join(map(str, temp)))
