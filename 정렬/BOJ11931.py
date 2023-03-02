import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort(reverse=True)

for ns in nums:
    print(ns)