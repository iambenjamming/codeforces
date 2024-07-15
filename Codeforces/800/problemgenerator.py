t = int(input())

for _ in range(t):
    
    n, m = [x for x in map(int, input().split())]

    problems = input()

    keys = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

    dictionary = {key: 0 for key in keys}

    count = 0

    for char in problems:
        if char in keys:
            dictionary[char] += 1

    for num in dictionary.values():
        if num < m:
            count += m - num

    print(count)
