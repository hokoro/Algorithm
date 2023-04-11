import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

dp = []

nums = []

for i,j in zip(a,b):
    nums.append(alpha[ord(i) % 65])
    nums.append(alpha[ord(j) % 65])

dp.append(nums)
index = 0
while True:
    if len(dp[-1]) == 2:
        break
    nums = []
    for i in range(len(dp[-1])-1):
        nums.append((dp[index][i] + dp[index][i+1]) % 10)

    index += 1
    dp.append(nums)

print(f'{dp[-1][0]}{dp[-1][1]}')
