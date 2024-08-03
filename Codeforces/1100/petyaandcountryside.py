n = int(input())
garden = list(map(int, input().split()))

flow = 1

for i in range(len(garden)):
    itleft = i-1
    itright = i+1
    count = 1

    if itleft >= 0:
        while(itleft >= 0):
            if garden[itleft] <= garden[itleft+1]:
                count += 1
                itleft -= 1
            else:
                break

    if itright < len(garden):
        while(itright < len(garden)):
            if garden[itright] <= garden[itright-1]:
                count += 1
                itright += 1
            else:
                break

    flow = max(flow, count)
    
print(flow)
    
