import sys
input = sys.stdin.readline
sum_ = 0
nums = []
for _ in range(10):
    num = int(input())
    sum_ += num
    if sum_ == 100:
        nums.append(sum_)
        break
    if len(nums) >0 and abs(100 - sum_) > abs(100 - nums[-1]):
        break
    if len(nums) > 0 and 100 < nums[-1] < sum_:
        break
    nums.append(sum_)

print(nums[-1])
