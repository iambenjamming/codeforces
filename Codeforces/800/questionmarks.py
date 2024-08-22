t = int(input())

for _ in range(t):

    n = int(input())

    s = input()

    ans = min(s.count('A'), n) + min(s.count('B'), n) + min(s.count('C'), n) + min(s.count('D'), n)

    print(ans)