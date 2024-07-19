s = input()

time = int(s, 2)

trains = [1, 0] * 50

if time > pow(2, len(s) - 1):
    print(trains[:len(s)].count(1))
else:
    print(trains[:len(s)-1].count(1))

