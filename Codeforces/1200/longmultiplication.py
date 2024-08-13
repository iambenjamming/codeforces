t = int(input())

for _ in range(t):

    x = input()
    y = input()

    num1 = []
    num2 = []

    index = 0
    more = False

    for i in range(len(x)):
        if int(x[i]) != int(y[i]):
            index = i
            more = True
            break
        else:
            num1.append(x[i])
            num2.append(y[i])

    if more:
        num1.append(max(int(x[index]), int(y[index])))
        num2.append(min(int(x[index]), int(y[index])))
        index += 1

        while (index < len(x)):
            num1.append(min(int(x[index]), int(y[index])))
            num2.append(max(int(x[index]), int(y[index])))
            index += 1

    print(''.join(map(str, num1)))
    print(''.join(map(str, num2)))
