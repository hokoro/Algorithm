from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())

graphs = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

spots = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graphs[i][j][k] == 1:
                spots.append([i, j, k])

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]


def bfs(spot, graph):
    queue = spot
    while queue:
        z, x, y = queue.popleft()
        for s in range(6):
            nx = x + dx[s]
            ny = y + dy[s]
            nz = z + dz[s]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                continue
            if graph[nz][nx][ny] == -1 or graph[nz][nx][ny] == 1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append((nz,nx,ny))


max_result = 0
bfs(spots, graphs)
for i in range(len(graphs)):
    for row in graphs[i]:
        for num in row:
            if num == 0:
                print(-1)
                exit(0)
        max_result = max(max_result, max(row))

print(max_result - 1)
