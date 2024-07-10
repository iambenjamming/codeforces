from sys import stdin, stdout

t = int(stdin.readline())

while (t > 0):

    n = int(stdin.readline())

    rudolph = stdin.readline()

    uglycount = 0

    

    if "mapie" not in rudolph:
        uglycount += rudolph.count("map")
        uglycount += rudolph.count("pie")
    else:
        uglycount += rudolph.count("mapie")
        uglycount += rudolph.count("map") - rudolph.count("mapie")
        uglycount += rudolph.count("pie") - rudolph.count("mapie")

    print(uglycount)

    t -= 1
