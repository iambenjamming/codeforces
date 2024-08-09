n = int(input())
b = list(map(int, input().split()))

if sum(b) & 1:
    print(sum(b))
else:
    yas = sum(b)

    b.sort()
    for e in b:
        if e&1:
            yas = e
            break

    print(sum(b)-yas)
