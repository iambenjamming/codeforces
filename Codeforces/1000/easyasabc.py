letters = [list(input().strip()) for _ in range(3)]

adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

combinations = set()

for r in range(3):
    for c in range(3):
        for adjr1, adjc1 in adj:
            posr1 = r + adjr1
            posc1 = c + adjc1
            if 0 <= posr1 < 3 and 0 <= posc1 < 3:
                for adjr2, adjc2 in adj:
                    posr2 = adjr2 + posr1
                    posc2 = adjc2 + posc1
                    if 0 <= posr2 < 3 and 0 <= posc2 < 3 and (posr2 != r or posc2 != c):
                        comb = letters[r][c] + letters[posr1][posc1] + letters[posr2][posc2]
                        combinations.add(comb)

print(min(combinations))
