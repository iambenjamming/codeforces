t = int(input())

for _ in range(t):
    n = int(input())
    word = input()

    ans = len(set(word))

    if len(word) == ans:
        print(len(word))
        continue
    
    check = []

    for i in range(n):
        if word[i] not in check:
            check.append(word[i])
            ans = max(ans, len(set(word[:i+1])) + len(set(word[i+1:])))

    print(ans)

