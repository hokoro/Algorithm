import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

max_dp = [1] * n
min_dp = [0] * n

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            max_dp[i] = max(max_dp[i], max_dp[j] + 1)
# print(max(max_dp))
idx = max_dp.index(max(max_dp))
for i in range(idx, n):
    for j in range(0, i):
        if nums[j] > nums[i]:
            min_dp[i] = max(min_dp[i], min_dp[j] + 1)

print(max(min_dp) + max(max_dp))

# print(max_dp)
# print(min_dp)
