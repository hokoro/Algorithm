import sys
import heapq

n,m = map(int,sys.stdin.readline().split())

nums = list(map(int,sys.stdin.readline().split()))
heap = []

for num in nums:
    heapq.heappush(heap,num)

while m != 0:
    min_ = heapq.heappop(heap)
    min2_ = heapq.heappop(heap)

    min_ = min_ + min2_

    heapq.heappush(heap,min_)
    heapq.heappush(heap,min_)
    m -= 1

print(sum(heap))