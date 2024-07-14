t = int(input())

for _ in range(t):

    binary = input()

    count0 = binary.count('0')
    count1 = binary.count('1')

    index = 0

    n = len(binary)
    loop = True

    for i in range(0, n):

        if binary[i] == '0':
            if count1 > 0:
                count1 -= 1
            else:
                index = i
                loop = False
                break
            

        elif binary[i] == '1':
            if count0 > 0:
                count0 -= 1
            else:
                index = i
                loop = False
                break
    if loop == True:
        index = n

    print(n - index)
