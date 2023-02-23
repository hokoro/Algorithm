import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = [i + 1 for i in range(1, n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    before = nums[i - 1:k]
    after = nums[k:j]
    nums[i - 1:j] = after + before

for num in nums:
    print(num, end=' ')
