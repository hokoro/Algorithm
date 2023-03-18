n = int(input())

for _ in range(n):
    num = int(input())
    dp = []

    for i in range(num+1):
        if i < 2:
            dp.append(1)
        elif i == 2:
            dp.append(2)
        elif i == 3:
            dp.append(4)
        else:
            dp.append(dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4])

    print(dp[num])
