n = int(input())
nums = list(map(int,input().split()))

MAX_ = max(nums)
if MAX_ > 50:
    print(0)

elif nums.count(50) > 0:
    fifty = nums.count(50)
    if fifty > 0:
        print(1)

else:
    answer = 0
    nums_set = list(set(nums))
    for num in nums_set:
        count = nums.count(num)
        answer += (count // 2)

    print(answer)
