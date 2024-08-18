t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    Bob = False

    if a == b:
        Bob = True
        
    if Bob == False:
        for i in range(n):
            if a[i] == b[-1-i]:
                Bob = True
            else:
                Bob = False
                break

    if Bob == True:
        print('Bob')
    else:
        print('Alice')

