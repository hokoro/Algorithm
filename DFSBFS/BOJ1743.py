import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n, m, k = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = dx[::-1]

graphs = [[True] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    graphs[x - 1][y - 1] = False

answers = []
cnt = 0


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graphs[x][y] == False and visited[x][y] == False:
            global cnt
            cnt += 1
            visited[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                dfs(nx, ny)
            return True
    return False


for i in range(n):
    for j in range(m):
        if graphs[i][j] == False and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            answers.append(cnt)

print(max(answers))
