t = int(input())

for _ in range(t):

    answer = "YES"

    x = input()

    if len(x) == 1:
        print("NO")
        continue
    if x[0] != '1':
        print("NO")
        continue
    if x[-1] == '9':
        print("NO")
        continue

    for i in range(1, len(x) - 1):
        if x[i] == '0':
            answer = "NO"
            break

    print(answer)
