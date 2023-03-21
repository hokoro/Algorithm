import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
counts = [[0] * m for _ in range(n)]

cnt = 0
MAX = 0

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

sharks = deque([])

for i in range(n):
    for j in range(m):
        if graphs[i][j] == 1:
            sharks.append((i, j))


def bfs():
    queue = sharks
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graphs[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                counts[nx][ny] = counts[x][y] + 1
                queue.append((nx, ny))


bfs()
MAX = 0
for row in counts:
    for i in row:
        if MAX < i:
            MAX = i
print(MAX)
