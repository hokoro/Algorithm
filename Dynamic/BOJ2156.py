import sys

input = sys.stdin.readline

dp = [0]

n = int(input())
nums = [int(input()) for _ in range(n)]

for i in range(len(nums)):
    if i == 0:
        dp.append(nums[i])
    elif i == 1:
        dp.append(nums[i - 1] + nums[i])
    elif i == 2:
        MAX = max(dp[i - 2], nums[i - 1] + nums[i], nums[i - 2] + nums[i])
        dp.append(MAX)
    else:
        MAX = max(dp[i - 1], dp[i - 3] + nums[i - 1] + nums[i], dp[i - 2] + nums[i])
        dp.append(MAX)

print(dp[-1])
