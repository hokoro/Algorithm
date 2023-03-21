import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())

graphs = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
o = 0  # 양
v = 0  # 늑대
animal = [0, 0]
dx = [-1, 0, 1, 0]
dy = dx[::-1]


def dfs(x, y):
    global o, v
    visited[x][y] = True
    if graphs[x][y] == 'o':
        o += 1
    if graphs[x][y] == 'v':
        v += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if graphs[nx][ny] != '#' and not visited[nx][ny]:
                dfs(nx, ny)


for i in range(n):
    for j in range(m):
        if graphs[i][j] != '#' and not visited[i][j]:
            dfs(i, j)
            if o > v:
                animal[0] += o
            else:
                animal[1] += v
            o, v = 0, 0
print(animal[0], animal[1])
