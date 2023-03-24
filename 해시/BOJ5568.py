import sys
from itertools import combinations,permutations
input = sys.stdin.readline

n = int(input())
k = int(input())

nums = [int(input()) for _ in range(n)]
used = []
coms = list(combinations(nums,k))

for com in coms:
    pers = list(permutations(com,k))
    for per in pers:
        token = ''
        for i in range(len(per)):
            token += str(per[i])

        if int(token) not in used:
            used.append(int(token))

print(len(used))
