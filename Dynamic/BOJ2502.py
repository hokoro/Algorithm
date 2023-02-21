import sys

input = sys.stdin.readline

dp = [[0,0],[1, 0], [0, 1]]
d, k = map(int, input().split())

for i in range(3, d + 1):
    a = dp[i-1][1]
    b = a + dp[i-1][0]
    dp.append([a,b])


A = 1
while True:
    K = k
    K -= dp[d][0] * A

    if K % dp[d][1] == 0:
        B = K // dp[d][1]
        break
    else:
        A += 1

print(A)
print(B)


