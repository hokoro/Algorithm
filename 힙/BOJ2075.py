import sys
import heapq
n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    nums = list(map(int,sys.stdin.readline().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap,num)
            continue
        if heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap,num)


print(heap[0])

