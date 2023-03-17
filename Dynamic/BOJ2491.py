import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

dp_1 = [1] * n

dp_2 = [1] * n

for i in range(1,n):
    if nums[i] >= nums[i-1]:
        dp_1[i] = dp_1[i-1] + 1

for i in range(1,n):
    if nums[i] <= nums[i-1]:
        dp_2[i] = dp_2[i-1] + 1

print(max(max(dp_1) , max(dp_2)))