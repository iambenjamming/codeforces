t = int(input())

for _ in range(t):

    base = input()
    reference = input()
    
    add = 0

    for c in range(len(reference)):

        j = 0
        i = c
        temp = 0

        while(i < len(reference) and j < len(base)):

            if base[j] == reference[i]:
                i += 1
                temp += 1

            j += 1

        add = max(add, temp)

    add = len(reference) - add

    print(len(base) + add)
    

    
