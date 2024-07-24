t = int(input())

for _ in range(t):

    abc = list(map(int, input().split()))

    operation = 5

    while(operation > 0):
        abc.sort()
        abc[0] += 1
        operation -= 1

    print(abc[0]*abc[1]*abc[2])