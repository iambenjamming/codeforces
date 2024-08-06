t = int(input())
 
for _ in range(t):
 
    cards = list(map(int, input().split()))
 
    ans = 0
 
    s1, s2, l1, l2 = cards[0], cards[1], cards[2], cards[3]
 
    if s1 > l1:
        if s2 > l2:
            ans += 1
    if s1 > l2:
        if s2 > l1:
            ans += 1
    if s1 > l1:
        if s2 == l2:
            ans += 1
    if s1 > l2:
        if s2 == l1:
            ans += 1
    if s1 == l1:
        if s2 > l2:
            ans += 1
    if s1 == l2:
        if s2 > l1:
            ans += 1
    if s2 > l1:
        if s1 > l2:
            ans += 1
    if s2 > l2:
        if s1 > l1:
            ans += 1
    if s2 > l2:
        if s1 == l1:
            ans += 1
    if s2 > l1:
        if s1 == l2:
            ans += 1
    if s2 == l1:
        if s1 > l2:
            ans += 1
    if s2 == l2:
        if s1 > l1:
            ans += 1
 
    print(ans)
