import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

max_dp = [1] * n
min_dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            max_dp[i] = max(max_dp[i], max_dp[j] + 1)

nums_r = nums[::-1]

for i in range(1,n):
    for j in range(0,i):
        if nums_r[j] < nums_r[i]:
            min_dp[i] = max(min_dp[i] , min_dp[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = max_dp[i] + min_dp[n-i-1] - 1

print(max(result))


