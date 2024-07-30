n = int(input())

scoreboard = {}
scores = []
names = []
highscore = 0
winner = ''

for _ in range(n):

    name, score = input().split(' ')

    names.append(name)
    scores.append(score)

    if name not in scoreboard:
        scoreboard[name] = int(score)
    else:
        scoreboard[name] += int(score)

for name in scoreboard:
    if scoreboard[name]>highscore:
        highscore = scoreboard[name]
        winners=[]
        winners.append(name)
    elif scoreboard[name]==highscore:
        winners.append(name)

namesnew = {}

if len(winners) == 1:
    print(winners[0])
else:
    for i in range(len(names)):
        flag = False
        for j in range(len(winners)):
            if winners[j] == names[i]:
                flag = True

        if flag == True:
            if names[i] not in namesnew:
                namesnew[names[i]] = int(scores[i]) 
            else:
                namesnew[names[i]] += int(scores[i])
            if namesnew[names[i]] >= highscore:
                print(names[i])
                break
