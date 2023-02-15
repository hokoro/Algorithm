import math

nums = list(map(int, input().split()))

start = min(nums)
answer = 0
count = 0

while True:
    for num in nums:
        if start % num == 0:
            count += 1

    if count >= 3:
        answer = start
        break

    else:
        start = start + 1
        count = 0

print(answer)

