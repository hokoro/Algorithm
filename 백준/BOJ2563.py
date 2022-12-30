test_case = int(input())
board = [[0 for j in range(100)] for i in range(100)]
answer = 0
two_count = 0
for _ in range(test_case):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            board[i][j] = 1

for row in board:
    answer += (row.count(1))
print(answer)
