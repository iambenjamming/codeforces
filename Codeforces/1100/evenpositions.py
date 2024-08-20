def magic(s):
    stack = []
    distances = []
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')' and stack:
            start = stack.pop()
            distance = i - start
            distances.append(distance)
    
    return sum(distances)

t = int(input())

for _ in range(t):

    n = int(input())
    s = list(c for c in input())

    s[0] = '('

    for i in range(1, n):
        if i & 1 == 0:
            if s[i-1] == '(':
                s[i] = ')'
            else:
                s[i] = '('

    print(magic(s))
