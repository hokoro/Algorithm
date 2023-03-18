import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:  # 1로 오는것 밖에 안받는다
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)

# nums = [list(range(1, 10))]
#
# dp.append(len(nums[-1]))
#
# for i in range(1, n):
#     token = []
#     for num in nums[-1]:
#         t = int(str(num)[-1])
#         if t - 1 >= 0:
#             token.append(int(str(num) + str(t - 1)))
#         if t + 1 < 10:
#             token.append(int(str(num) + str(t + 1)))
#
#     dp.append(len(token))
#     nums.append(token)
# print(dp[n-1])
