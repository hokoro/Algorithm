import sys
input = sys.stdin.readline

t = int(input())
answers = []
for _ in range(t):
    nums = list(map(int,input().split()))
    nums.remove(max(nums))
    nums.remove(min(nums))
    if max(nums) - min(nums) >= 4:
        answers.append('KIN')
    else:
        answers.append(sum(nums))

for answer in answers:
    print(answer)