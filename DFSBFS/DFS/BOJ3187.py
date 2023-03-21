import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def dfs(x, y):
    global W, S
    visited[x][y] = True
    if graphs[x][y] == 'v':
        W += 1
    if graphs[x][y] == 'k':
        S += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graphs[nx][ny] != '#':
                dfs(nx, ny)


Ws = 0
Ss = 0

W = 0
S = 0

for i in range(n):
    for j in range(m):
        if graphs[i][j] != '#' and visited[i][j] == False:
            dfs(i, j)
            if W >= S:
                Ws += W
            else:
                Ss += S
            W, S = 0, 0

print(Ss, Ws)
