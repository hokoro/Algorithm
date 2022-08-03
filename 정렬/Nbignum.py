t = int(input())
answer = []
for _ in range(t):
    nums = list(map(int,input().split()))

    nums.sort(reverse=True)

    answer.append(nums[2])


for ans in answer:
    print(ans , end = '\n')
