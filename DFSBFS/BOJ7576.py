from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
spot = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            spot.append([i, j])
dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(spots, graph):
    queue = spots
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs(spot, graph)
max_result = 0
for row in graph:
    for num in row:
        if num == 0:
            print(-1)
            exit(0)
    max_result = max(max_result, max(row))

print(max_result - 1)
