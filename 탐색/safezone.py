def solution(board):
    board_size = len(board) * len(board[0])
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                count += 1
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if x < 0 or x > len(board) - 1 or y < 0 or y > len(board[i]) - 1:
                            continue
                        else:
                            if board[x][y] == 'x' or board[x][y] ==1:
                                continue
                            else:
                                board[x][y] = 'x'
                                count += 1

    return board_size - count


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
print(solution(board))

board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
print(solution(board))
