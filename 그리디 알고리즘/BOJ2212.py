import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

nums = list(map(int,input().split()))

nums.sort()

differs = []
for i in range(len(nums) -1):
    differs.append(nums[i+1] - nums[i])


differs.sort(reverse=True)

print(sum(differs[k-1:]))