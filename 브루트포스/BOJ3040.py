from itertools import combinations
import sys
input = sys.stdin.readline
nums = []

for _ in range(9):
    num = int(input())
    nums.append(num)


coms = list(set(combinations(nums,7)))

for com in coms:
    if sum(com) == 100:
        for token in com:
            print(token)