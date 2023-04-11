import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[False] * n for _ in range(n)]
count = [[0] * n for _ in range(n)]


def bfs(x, y):
    visited[x][y] = True
    queue = deque([])
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return count[x][y]
        for i in range(6):
            nr = x + dx[i]
            nc = y + dy[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                count[nr][nc] = count[x][y] + 1
                queue.append((nr, nc))
    if count[r2][c2] == 0:
        return -1


print(bfs(r1, c1))
