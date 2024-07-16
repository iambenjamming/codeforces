matrix = []

# Read 5 lines of input, one for each row of the matrix
for _ in range(5):
    lines = input()
    matrix.append(list(map(int, lines.split())))

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(2-i)+abs(2-j))
