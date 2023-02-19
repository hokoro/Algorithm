import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))

