import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

s, x, y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, time, i, j = q.popleft()

    if time == s:
        break
    for l in range(4):
        nx = i + dx[l]
        ny = j + dy[l]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(graph[x - 1][y - 1])
