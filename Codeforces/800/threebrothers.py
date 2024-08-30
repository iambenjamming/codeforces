b = list(map(int, input().split()))

reference = [1, 2, 3]

for e in b:
    if e in b :
        reference.remove(e)
    
print(*reference)