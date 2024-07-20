t = int(input())

for _ in range(t):

    x, y = [i for i in list(map(int, input().split()))]

    XOR = x ^ y
    binary = bin(XOR)
    binstring = binary[2:]

    rev = ''.join(reversed(binstring))

    index = 0

    for i in range(len(rev)):
        if rev[i] == '1':
            index = i
            break
        
    print(pow(2, index))