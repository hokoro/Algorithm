import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    answer = 0
    max_val = 0

    for i in range(n-1,-1 ,-1):
        if nums[i] > max_val:
            max_val = nums[i]

        else:
            answer += max_val - nums[i]


    print(answer)