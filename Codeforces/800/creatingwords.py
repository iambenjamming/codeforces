t = int(input())

while (t > 0):

    words = input().split()

    first = words[0].split()
    second = words[1].split()

    newfirst = words[1][0] + words[0][1] + words[0][2]
    newsecond = words[0][0] + words[1][1] + words[1][2]

    print(newfirst, newsecond) 

    t -= 1
