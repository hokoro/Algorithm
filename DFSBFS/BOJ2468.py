from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)

dx = [-1, 0, 1, 0]
dy = dx[::-1]
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

MAX = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if MAX < graph[i][j]:
            MAX = graph[i][j]

max_result = 0


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] > i:
                queue.append((nx, ny))
                visited[nx][ny] = 1


for i in range(1, MAX + 1):
    count = 0
    visited = [[0] * n for _ in range(n + 1)]
    for j in range(len(graph)):
        for k in range(len(graph[j])):
            if graph[j][k] > i and visited[j][k] == 0:
                count += 1
                bfs(j, k)
    if max_result < count:
        max_result = count

print(max_result)