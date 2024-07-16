n = int(input())

luckynum = [4, 7, 47, 74, 44, 444, 447, 474, 477, 777, 774, 744]

lucky = False

for num in luckynum:
    if n % num == 0:
        lucky = True

if lucky == True:
    print("YES")
else:
    print("NO")