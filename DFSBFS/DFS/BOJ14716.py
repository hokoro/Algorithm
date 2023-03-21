import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)
cnt = 0
m, n = map(int, input().split())
graphs = []
visited = [[0] * n for _ in range(m)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for _ in range(m):
    nums = list(input().strip().split())
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    graphs.append(nums)


def dfs(x, y):
    visited[x][y] = cnt
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graphs[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)


for i in range(m):
    for j in range(n):
        if graphs[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i, j)

print(cnt)