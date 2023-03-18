import sys
input = sys.stdin.readline
n = int(input())

nums = [float(input()) for _ in range(n)]
dp = nums[:]

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if dp[j] <= dp[j - 1] * nums[j]:
            dp[j] = dp[j - 1] * nums[j]
        else:
            break

print('{:.3f}'.format(max(dp)))
