import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

R_move = [0, 1]
C_move = [1, 0]


def dfs(x, y):
    global R_cnt,C_cnt

    if graphs[x][y] == '-':
        visited[x][y] = R_cnt

        nx = x + R_move[0]
        ny = y + R_move[1]

        if 0 <= nx < n and 0 <= ny < m:
            if graphs[nx][ny] == '-' and visited[nx][ny] == 0:
                dfs(nx,ny)

    if graphs[x][y] == '|':
        visited[x][y] = C_cnt

        nx = x + C_move[0]
        ny = y + C_move[1]

        if 0 <= nx < n and 0 <= ny < m:
            if graphs[nx][ny] == '|' and visited[nx][ny] == 0:
                dfs(nx, ny)


R_cnt = 0
C_cnt = 0
for i in range(n):
    for j in range(m):
        if graphs[i][j] == '-' and visited[i][j] == 0:
            R_cnt += 1
            dfs(i, j)

        if graphs[i][j] == '|' and visited[i][j] == 0:
            C_cnt += 1
            dfs(i, j)

print(R_cnt + C_cnt)

