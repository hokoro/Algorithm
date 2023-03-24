import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

for num in nums:
    print(num - n * k, end=' ')
