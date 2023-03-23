import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = dx[::-1]

n, m = map(int, input().split())
graphs = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
counts = [[0] * m for _ in range(n)]


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if graphs[x][y] in [3, 4, 5]:
            return graphs[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graphs[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False


for i in range(n):
    for j in range(m):
        graphs[i][j] = int(graphs[i][j])

for i in range(n):
    for j in range(m):
        if graphs[i][j] == 2 and not visited[i][j]:
            ans = bfs(i, j)
            if not ans:
                print('NIE')
            else:
                print('TAK')
                print(ans)
            break
