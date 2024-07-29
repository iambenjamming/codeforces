rook = input()
rx, ry = ord(rook[0]) - ord('a'), int(rook[1])-1

knight = input()
kx, ky = ord(knight[0]) - ord('a'), int(knight[1])-1

board = [[0] * 8 for _ in range(8)] #board[x][y]

for i in range(8):
    board[i][ry] = 1
    board[rx][i] = 1

#knight sqaures
board[kx][ky] = 1
if 0 <= kx - 2 < 8 and 0 <= ky + 1 < 8:
    board[kx - 2][ky + 1] = 1
if 0 <= kx - 2 < 8 and 0 <= ky - 1 < 8:
    board[kx - 2][ky - 1] = 1
if 0 <= kx + 2 < 8 and 0 <= ky + 1 < 8:
    board[kx + 2][ky + 1] = 1
if 0 <= kx + 2 < 8 and 0 <= ky - 1 < 8:
    board[kx + 2][ky - 1] = 1
if 0 <= kx - 1 < 8 and 0 <= ky + 2 < 8:
    board[kx - 1][ky + 2] = 1
if 0 <= kx + 1 < 8 and 0 <= ky + 2 < 8:
    board[kx + 1][ky + 2] = 1
if 0 <= kx + 1 < 8 and 0 <= ky - 2 < 8:
    board[kx + 1][ky - 2] = 1
if 0 <= kx - 1 < 8 and 0 <= ky - 2 < 8:
    board[kx - 1][ky - 2] = 1

#rook vulnerable squares
if 0 <= rx - 2 < 8 and 0 <= ry + 1 < 8:
    board[rx - 2][ry + 1] = 1
if 0 <= rx - 2 < 8 and 0 <= ry - 1 < 8:
    board[rx - 2][ry - 1] = 1
if 0 <= rx + 2 < 8 and 0 <= ry + 1 < 8:
    board[rx + 2][ry + 1] = 1
if 0 <= rx + 2 < 8 and 0 <= ry - 1 < 8:
    board[rx + 2][ry - 1] = 1
if 0 <= rx - 1 < 8 and 0 <= ry + 2 < 8:
    board[rx - 1][ry + 2] = 1
if 0 <= rx + 1 < 8 and 0 <= ry + 2 < 8:
    board[rx + 1][ry + 2] = 1
if 0 <= rx + 1 < 8 and 0 <= ry - 2 < 8:
    board[rx + 1][ry - 2] = 1
if 0 <= rx - 1 < 8 and 0 <= ry - 2 < 8:
    board[rx - 1][ry - 2] = 1
    
print(sum(row.count(0) for row in board))
