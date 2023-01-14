people = int(input())
use_time = list(map(int, input().split()))
accumulated_time = []
sum_time = 0
use_time.sort()

for time in use_time:
    sum_time = sum_time + time
    accumulated_time.append(sum_time)

print(sum(accumulated_time))
