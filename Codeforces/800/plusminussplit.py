t = int(input())

for _ in range(t):

    n = int(input())

    s = list(x for x in input())

    add = s.count('+')
    minus = s.count('-')

    print(abs(add-minus))
