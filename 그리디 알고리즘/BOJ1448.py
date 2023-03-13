import sys

input = sys.stdin.readline

n = int(input())

nums = sorted([int(input()) for _ in range(n)], reverse=True)

answer = -1
for i in range(len(nums)- 2):
    if nums[i] < nums[i+1] + nums[i+2]:
        answer = nums[i] + nums[i+1] + nums[i+2]
        break
print(answer)