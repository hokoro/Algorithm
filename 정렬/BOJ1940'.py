import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int,input().split()))
nums.sort()
answer = 0
left = 0
right = len(nums)-1
while left < right:
    if nums[left] + nums[right] == m:
        answer += 1
        left += 1
        right -=1
    elif nums[left] + nums[right] < m:
        left += 1

    else:
        right -= 1

print(answer)