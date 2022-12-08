board = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    for j in range(19):
        if board[a-1][j] == 1:
            board[a-1][j] = 0
        else:
            board[a-1][j] = 1

        if board[j][b-1] == 1:
            board[j][b-1] = 0
        else:
            board[j][b-1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print('')
