from collections import Counter

t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    num = Counter(a)
    answered = False

    for n in num:
        if num[n]&1 == 1:
            print("YES")
            answered = True
            break

    if answered == False:
        print("NO")