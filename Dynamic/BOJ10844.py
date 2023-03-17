import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 , [1] * 9]]

nums = [list(range(1, 10))]

dp.append(len(nums[-1]))

for i in range(1, n):
    token = []
    for num in nums[-1]:
        t = int(str(num)[-1])
        if t - 1 >= 0:
            token.append(int(str(num) + str(t - 1)))
        if t + 1 < 10:
            token.append(int(str(num) + str(t + 1)))

    dp.append(len(token))
    nums.append(token)
print(dp[n-1])

