import math
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        print('0')
        
    elif a > b:
        print(math.ceil((a-b)/10))
    elif a < b:
        print(math.ceil((b-a)/10))