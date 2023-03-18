import sys

input = sys.stdin.readline

MAX = 1000000009
dp = [0] * 1000000
dp[0] = 1
dp[1] = 2
dp[2] = 4
n = int(input())
nums = [int(input()) for _ in range(n)]
max_ = max(nums)

for i in range(3,max_):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MAX

for num in nums:
    print(dp[num-1])