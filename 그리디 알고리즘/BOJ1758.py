import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort(reverse=True)

answer = 0
for i in range(len(nums)):
    if nums[i] - i > 0:
        answer += (nums[i] - (i+1-1))
print(answer)