n = int(input())
board = [[0 for j in range(19)] for i in range(19)]

for i in range(n):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end=' ')
    print('')

