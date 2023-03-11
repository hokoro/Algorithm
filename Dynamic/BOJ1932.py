import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * len(nums[i]) for i in range(len(nums))]

for i in range(n):
    if i == 0:
        for j in range(len(nums[i])):
            dp[i][j] = nums[i][j]
    elif i == 1:
        for j in range(len(nums[i])):
            dp[i][j] = dp[i-1][0] + nums[i][j]
    else:
        for j in range(len(nums[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + nums[i][j]
            elif j == len(nums[i]) -1:
                dp[i][j] = dp[i-1][j-1] + nums[i][j]
            else:
                a = dp[i-1][j-1] + nums[i][j]
                b = dp[i-1][j] + nums[i][j]
                dp[i][j] = max(dp[i][j],a,b)

print(max(dp[-1]))







