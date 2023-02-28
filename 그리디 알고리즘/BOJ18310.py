import sys
input = sys.stdin.readline

t = int(input())
nums = list(map(int,input().split()))
nums.sort()
answer = 0
if len(nums) % 2 ==0:
    answer = nums[len(nums) // 2 -1]

else:
    answer = nums[len(nums) // 2]

print(answer)