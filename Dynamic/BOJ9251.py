import sys

input = sys.stdin.readline
s1 = " " + input().strip()
s2 = " " + input().strip()
n, m = len(s1) - 1, len(s2) - 1
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[n][m])

result = []

i = n
j = m
while True:
    if dp[i][j] == 0:
        break

    elif dp[i - 1][j] == dp[i][j]:
        i = i - 1

    elif dp[i][j - 1] == dp[i][j]:
        j = j - 1

    else:
        result.append(s1[i])
        i -= 1
        j -= 1

print(''.join(result[::-1]))
