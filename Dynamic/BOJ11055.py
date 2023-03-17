n = int(input())

nums = list(map(int, input().split()))

dp = nums[:] # 가장 큰 증가를 봐야 하기 때문에 입력값으로 dp 를 잡는다

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
print(max(dp))
