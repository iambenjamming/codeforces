from sys import stdin, stdout

word = stdin.readline()

vowels = {'A', 'a', 'O', 'o', 'Y', 'y', 'E', 'e', 'U', 'u', 'I', 'i'}
uppercase = {}

newletters = []

a = len(word) - 1

for c in word:
    if c == '\n':
        continue
    if c in vowels:
        continue
    if c.isupper():
        subword = '.' + c.lower()
        newletters.append(subword)
        continue
    if c not in vowels:
        subword = '.' + c
        newletters.append(subword)

newword = ''.join(newletters)


print(newword)
        
