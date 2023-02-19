import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]

com = list(combinations(nums, m))

for token in com:
    for j in range(len(token)):
        print(token[j], end=' ')
    print()
