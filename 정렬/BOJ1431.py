import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    number = input().rstrip()
    sum_ = 0
    for i in number:
        if i.isdigit():
            sum_ += int(i)

    nums.append([len(number), sum_, number])

nums.sort(key=lambda x: [x[0], x[1],x[2]])

for num in nums:
    print(num[2])