from sys import stdin, stdout

t = int(stdin.readline())

answers = []

for _ in range(t):

    q = int(stdin.readline())

    qarr = list(map(int, stdin.readline().strip().split()))

    barr = []

    ans = []

    inserted = False

    for i in qarr:
        if len(barr) == 0 or i >= barr[-1] or i <= barr[0] and not inserted:
            if inserted and i > barr[0]:
                ans.append('0')
            else:
                barr.append(i)
                ans.append('1')
            if len(barr) > 1 and i < barr[-2]:
                inserted = True
        else:
            ans.append('0')

    answers.append(''.join(ans))

stdout.write('\n'.join(answers))
