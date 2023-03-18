import sys

input = sys.stdin.readline

dp = [1]

n = int(input())


for i in range(1,n+1):
    if i == 1:
        dp.append(dp[i-1] * dp[i-1])
    else:
        sum_ = 0
        for j in range(0,i):
            sum_ += (dp[j] * dp[i-1-j])

        dp.append(sum_)

print(dp[-1])