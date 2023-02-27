import sys
input = sys.stdin.readline

count = int(input())
nums = list(map(int,input().split()))
MAX = max(nums)
answer = 0
for i in range(1,MAX+1):
    if i not in nums:
        answer = i
        break


print(answer)