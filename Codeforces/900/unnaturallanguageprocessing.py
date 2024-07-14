import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())

    word = input()
    answer = []

    V = ['a', 'e']
    C = ['b', 'c', 'd']

    for i in range(0, len(word)):
        if word[i] in C:
            if (i-1) >= 0 and (i+1) < n:
                if (word[i-1] in V and word[i+1] in V) or (word[i-1] in C and word[i+1] in V):
                    answer.append('.'+word[i])
                else:
                    answer.append(word[i])
            else:
                    answer.append(word[i])
        else:
            answer.append(word[i])

    sys.stdout.write(''.join(answer)+'\n')
        
            

