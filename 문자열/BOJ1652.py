import sys
input = sys.stdin.readline

row = 0
col = 0

n = int(input())
board = [list(map(str,input().rstrip())) for _ in range(n)]


for b in board:
    token = ''
    for i in range(len(b)):
        if b[i] == '.':
            token += b[i]

        if b[i] == 'X':
            if len(token) >= 2:
                row += 1
                token = ''

            else:
                token = ''
    if len(token) >= 2:
        row += 1

for i in range(len(board)):
    token = ''
    for j in range(len(board[i])):
        if board[j][i] == '.':
            token += '.'

        if board[j][i] == 'X':
            if len(token) >= 2:
                col += 1
                token = ''
            else:
                token = ''
    if len(token) >= 2:
        col += 1

print(f'{row} {col}')
