import sys

input = sys.stdin.readline

dx = [1, 0, 1]
dy = [0, 1, 1]

n, m = map(int, input().split())

boards = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
dp[0][0] = boards[0][0]

for i in range(n):
    for j in range(m):
        for k in range(3):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if dp[nx][ny] < dp[i][j] + boards[nx][ny]:
                    dp[nx][ny] = dp[i][j] + boards[nx][ny]

print(dp[n-1][m-1])
