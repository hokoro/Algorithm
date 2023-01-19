def solution(keyinput, board):
    answer = []
    startpoint = [board[0] // 2, board[1] // 2]
    movepoint = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    for inkey in keyinput:
        if 0 <= startpoint[0] + movepoint[inkey][0] < board[0] and 0 <= startpoint[1] + movepoint[inkey][1] < board[1]:
            startpoint[0] = startpoint[0] + movepoint[inkey][0]
            startpoint[1] = startpoint[1] + movepoint[inkey][1]

    return [startpoint[0] - board[0]//2 , startpoint[1] - board[1]//2]


print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
