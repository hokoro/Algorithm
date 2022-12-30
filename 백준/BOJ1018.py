import sys

x, y = map(int, input().split())

board = [list(map(str, sys.stdin.readline())) for _ in range(x)]

ranges = [[i, j] for j in range(y - 7) for i in range(x - 7)]

UDLR = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer_list = []

for spot in ranges:
    count = 0
    temporary = board[spot[0]:spot[0] + 8][spot[0]:spot[1] + 8]
    for i in range(len(temporary)):
        for j in range(len(temporary[i])):
            for sp in UDLR:
                if i + sp[0] < 0 or i + sp[0] > len(temporary) or j + sp[1] < 0 or j + sp[1] > len(temporary[i]):
                    continue

                else:
                    if temporary[i][j] == 'B' and temporary[i][j] == temporary[i + sp[0]][j + sp[1]]:
                        temporary[i + sp[0]][i + sp[1]] = 'W'
                        count += 1
                        continue
                    if temporary[i][j] == 'W' and temporary[i][j] == temporary[i + sp[0]][j + sp[1]]:
                        temporary[i + sp[0]][i + sp[1]] = 'B'
                        count += 1
                        continue

    answer_list.append(count)

print(min(answer_list))
