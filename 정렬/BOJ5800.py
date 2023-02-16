import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())

for i in range(t):
    nums = list(map(int,input().split()))
    max_num = max(nums[1:])
    min_num = min(nums[1:])

    nums_re = sorted(nums[1:],reverse=True)
    largest_gap = 0
    for j in range(len(nums_re)-1):
        if largest_gap < nums_re[j] - nums_re[j+1]:
            largest_gap = nums_re[j] - nums_re[j+1]

    print(f'Class {i+1}')
    print(f'Max {max_num}, Min {min_num}, Largest gap {largest_gap}')
