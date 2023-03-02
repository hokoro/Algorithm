import sys
input = sys.stdin.readline
answer = 0
n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

for i in range(len(nums)):
    answer += abs(nums[i] - (i+1))

print(answer)