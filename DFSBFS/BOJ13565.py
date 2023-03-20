import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

m, n = map(int, input().split())

graphs = [list(input().strip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = dx[::-1]

for i in range(m):
    for j in range(n):
        graphs[i][j] = int(graphs[i][j])


def dfs(x, y):
    global cnt
    visited[x][y] = cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if graphs[nx][ny] == 0 and not visited[nx][ny]:
                dfs(nx, ny)


cnt = 1
for i in range(m):
    for j in range(n):
        if graphs[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            cnt += 1

flag = False
for i in range(1,cnt+1):
    if visited[0].count(i) > 0 and visited[-1].count(i) > 0:
        flag = True

if flag:
    print('YES')
else:
    print('NO')
