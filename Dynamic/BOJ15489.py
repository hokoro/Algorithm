import sys

input = sys.stdin.readline

r, c, w = map(int, input().split())
start = 1
dp = []

for i in range(0, r + w + 1):
    token = []
    for j in range(i):
        if j == 0:
            token.append(1)
            continue
        elif j == i - 1:
            token.append(1)
            continue
        else:
            token.append(dp[i - 1][j - 1] + dp[i - 1][j])
    dp.append(token)

cnt = 1
sum_ = 0
for i in range(r, r + w):
    for j in range(cnt):
        sum_ += dp[i][c - 1 + j]
    cnt += 1

print(sum_)
