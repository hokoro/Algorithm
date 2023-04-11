import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = dx[::-1]

n, m = map(int, input().split())

graphs = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = 0


def bfs(x, y):
    global ans
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if graphs[x][y] == 'P':
            ans += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graphs[nx][ny] != 'X' and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


for i in range(n):
    for j in range(m):
        if graphs[i][j] == 'I':
            bfs(i, j)

if ans != 0:
    print(ans)
else:
    print('TT')