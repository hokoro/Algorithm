import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
n, m = map(int, input().split())

graphs = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
counts = [[0] * n for _ in range(m)]

hx = [-2, -1, 1, 2, -2, -1, 1, 2]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(x, y):
    global k
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        if k > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if graphs[nx][ny] != 1 and not visited[nx][ny]:
                        counts[nx][ny] = counts[x][y] + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        k -= 1
        else:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < m and 0 <= ny < n:
                    if graphs[nx][ny] != 1 and not visited[nx][ny]:
                        counts[nx][ny] = counts[x][y] + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny))


bfs(0, 0)
print(graphs)
print(counts)
print(visited)
print(k)
if counts[m - 1][n - 1] == 0:
    print(-1)
else:
    print(counts[m - 1][n - 1])
