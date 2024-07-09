import sys
from sys import stdin, stdout

t = int(stdin.readline())

while (t > 0):

    n = int(stdin.readline())
    strengths = list(map(int, stdin.readline().split()))

    bigboy = float('-inf')
    eh = float('-inf')
    difference = []

    for strength in strengths:
        if strength > bigboy:
            eh = bigboy
            bigboy = strength
        elif strength > eh:
            eh = strength
    
    for strength in strengths:
        if strength == bigboy:
            difference.append(strength - eh)
        else:
            difference.append(strength - bigboy)

    stdout.write(' '.join(map(str, difference)) + '\n')
        
    t -= 1



    
