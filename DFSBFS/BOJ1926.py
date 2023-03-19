import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
n, m = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = dx[::-1]


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if nums[x][y] == 1 and not visited[x][y]:
            global cnt
            cnt += 1
            visited[x][y] = True
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                dfs(nx, ny)
            return True
    return False


answers = []
cnt = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            answers.append(cnt)


if len(answers) == 0:
    print(len(answers))
    print(0)
else:
    print(len(answers))
    print(max(answers))
