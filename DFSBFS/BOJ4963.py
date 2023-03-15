from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]


def bfs(x, y):
    global graph
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                graph[nx][ny] = 0
                visited[nx][ny] = 1
                queue.append((nx, ny))


while True:
    w, h = map(int, input().split())
    answer = 0
    if w == h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1 and visited[i][j] == 0:
                answer += 1
                graph[i][j] = 0
                bfs(i,j)
    print(answer)