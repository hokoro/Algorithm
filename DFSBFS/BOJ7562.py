import sys
from collections import deque


dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x, y, x_end, y_end):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            return visited[x][y]-1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    L = int(input())
    visited = [[0] * L for _ in range(L)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        print(bfs(start_x, start_y,end_x,end_y))
