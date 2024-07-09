from sys import stdin, stdout
import string

t = int(stdin.readline())

while (t > 0):

    n = int(stdin.readline())
    alphabet = list(string.ascii_lowercase)

    s = input()
    orderedword = sorted(s)

    last_letter = orderedword[n-1]
    matching_index = [index for index, letter in enumerate(alphabet) if letter == last_letter]

    for index in matching_index:
        print(index + 1)
    
    t -= 1
    
