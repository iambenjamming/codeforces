from sys import stdin, stdout

t = int(stdin.readline())

while (t > 0):

    nums = stdin.readline().split()
    x1 = int(nums[0])
    x2 = int(nums[1])
    x3 = int(nums[2])

    dis1 = abs(x1 - x2) + abs(x1 - x3)
    dis2 = abs(x2 - x1) + abs(x2 - x3)
    dis3 = abs(x3 - x1) + abs(x3 - x2)

    shortest = min(dis1, dis2, dis3)

    print(shortest)

    t -= 1
