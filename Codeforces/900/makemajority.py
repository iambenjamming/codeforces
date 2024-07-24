t = int(input())

for _ in range(t):

    n = int(input())

    a = input()

    count1 = a.count('1')
    row0 = 0
    currentis0 = False

    for char in a:
        if char == '0':
            if currentis0 == False:
                row0 += 1
                currentis0 = True
            
        elif char == '1':
            currentis0 = False
            
    if count1 > row0:
        print("YES")
    else:
        print("NO")
