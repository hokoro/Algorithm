n = int(input()) # 입력 숫자

nums = [0] * 10000

for i in range(n):
    nums[i] = int(input())


dp = [0] * 10000

dp[0] = nums[0]
dp[1] = nums[0] + nums[1]

dp[2] = max(nums[2] + nums[0] , nums[2] + nums[1],dp[1])

for i in range(3,n):
    dp[i] = max(nums[i] + dp[i-2] , nums[i] + nums[i-1] + dp[i-3] , dp[i-1])


print(max(dp))