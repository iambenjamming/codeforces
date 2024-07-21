n = int(input())
if n < 3:
    print("-1")
else:
    base = 10**(n-1)
    remainder = base % 210
    answer = base + (210 - remainder) % 210
    print(answer)
