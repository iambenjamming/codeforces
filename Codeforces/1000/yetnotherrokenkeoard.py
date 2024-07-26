t = int(input())
 
for _ in range(t):
 
    word = input()
 
    small_ind = []
    big_ind = []
    answer = []
 
    for i in range(len(word)):
        if word[i] != 'b' and word[i] != 'B':
            if word[i].isupper():
                big_ind.append(i)
            elif word[i].islower():
                small_ind.append(i)
        else:
            if word[i] == 'b' and len(small_ind) > 0:
                small_ind.pop()
            elif word[i] == 'B' and len(big_ind) > 0:
                big_ind.pop()
                
    answer_ind = small_ind + big_ind
    answer_ind.sort()
    for i in range(len(answer_ind)):
        answer.append(word[answer_ind[i]])
    print(''.join(answer))