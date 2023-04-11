import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

boards = [list(input().strip()) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def dfs(x, y, target):
    if 0 <= x < m and 0 <= y < n:
        if boards[x][y] == target and visited[x][y] == False:
            global cnt
            cnt += 1
            visited[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                dfs(nx, ny, target)
            return True
    return False


WS = 0
BS = 0
cnt = 0
for i in range(m):
    for j in range(n):
        if boards[i][j] == 'W':
            dfs(i, j, 'W')
            WS += (cnt ** 2)
        if boards[i][j] == 'B':
            dfs(i, j, 'B')
            BS += (cnt ** 2)
        cnt = 0

print(WS, BS)
