y = input()

n = len(y)

temp = int(y)

while 1:
    temp += 1
    if n == len(set([x for x in str(temp)])):
        print(temp)
        break