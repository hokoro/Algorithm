MAX = 1000000

dp = [1] * (MAX + 1)

s = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1
for i in range(1, MAX + 1):
    # 누적 값 계산
    s[i] = s[i - 1] + dp[i]
n = int(input())
ans = []
for _ in range(n):
    a = int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans)) + '\n')
