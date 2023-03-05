import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

summary = 0
sum_list = [0]
for num in nums:
    summary += num
    sum_list.append(summary)
for i in range(len(nums)-k+1):

    print(sum_list[i+k] , sum_list[i])
    if sum_list[i + k] - sum_list[i] > answer:
        answer = sum_list[i + k] - sum_list[i]

print(answer)
