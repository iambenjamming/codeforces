def keepadd(n, count):
    
    new = 0
    count += 1
    
    for x in str(n):
        new += int(x)


    if len(str(new)) > 1:
        return keepadd(new, count)
    else:
        return count

n = input()

if len(n) == 1:
    print('0')
    exit()
    
print(keepadd(n, 0))
