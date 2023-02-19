import sys
from math import gcd

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
nums = []

n = int(input())

for _ in range(n):
    num = int(input())
    nums.append(num)

nums.sort(reverse=True)

nums_dif = []
gcd_ans = 0
for i in range(len(nums) - 1):
    nums_dif.append(nums[i] - nums[i + 1])
    if len(nums_dif) == 1:
        gcd_ans = nums_dif[-1]
        continue
    else:
        gcd_ans = gcd(gcd_ans, nums_dif[-1])

result = set()
for i in range(2, int(gcd_ans ** 0.5) + 1):
    if gcd_ans % i == 0:
        result.add(i)
        result.add(gcd_ans // i)

result.add(gcd_ans)
print(*sorted(list(result)))
