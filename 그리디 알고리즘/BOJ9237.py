import sys
input = sys.stdin.readline

num = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
max_day = 0

for i in range(num):
    candidate = nums[i] + i + 1
    if candidate > max_day:
        max_day = candidate

print(max_day + 1)