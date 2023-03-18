import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    count = int(input())

    nums = list(map(int,input().split()))
    dp = nums[:]
    for i in range(count-1):
        for j in range(i+1,count):
            if dp[j] <= dp[j-1] + nums[j]:
                dp[j] = dp[j-1] + nums[j]
            else:
                break
    print(max(dp))