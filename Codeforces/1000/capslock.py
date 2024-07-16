import string

word = input()

uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)
newword = []

firstupper = False
count = 0

if word[0] in uppercase_letters:
    firstupper = True

for i in range(1, len(word)):
    if word[i] in uppercase_letters:
        count += 1

if (firstupper == False and count == len(word) - 1):
    newword.append(word[0].upper())
    for i in range(1, len(word)):
        newword.append(word[i].lower())

    print(''.join(newword))
elif (firstupper == True and count == len(word) - 1):
    newword.append(word[0].lower())
    for i in range(1, len(word)):
        newword.append(word[i].lower())

    print(''.join(newword))
else:
    print(word)
