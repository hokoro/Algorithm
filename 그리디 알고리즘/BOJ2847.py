import sys

input = sys.stdin.readline
answer = 0
t = int(input())
nums = []
for _ in range(t):
    num = int(input())
    nums.append(num)

for i in range(len(nums) - 2, -1, -1):
    if nums[i + 1] - 1 <= nums[i]:
        answer += (nums[i] - (nums[i + 1] - 1))
        nums[i] = nums[i + 1] - 1
        continue


print(answer)
