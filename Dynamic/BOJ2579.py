n = int(input())
nums = [0] * n

for i in range(n):
    nums[i] = int(input())

dp = [0] * n

if len(nums) <= 2:
    print(sum(nums))
else:
    dp[0] = nums[0]
    dp[1] = dp[0] + nums[1]

    for i in range(2,n):
        dp[i] = max(dp[i-2] + nums[i] , dp[i-3] + nums[i-1] + nums[i])

    print(dp[n-1])
