import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
counts = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graphs[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    counts[nx][ny] = counts[x][y] + 1
                    queue.append((nx, ny))


for i in range(len(graphs)):
    for j in range(len(graphs[i])):
        if graphs[i][j] == 2:
            bfs(i, j)
            break

for i in range(len(graphs)):
    for j in range(len(graphs[i])):
        if graphs[i][j] == 1 and not visited[i][j]:
            print(-1, end=' ')
        else:
            print(counts[i][j], end=' ')
    print()
