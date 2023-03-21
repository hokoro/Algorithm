import heapq

n = int(input())
heap_list = []
end = [0]
for _ in range(n):
    num = list(map(int, input().split()))
    heapq.heappush(heap_list, num)

for _ in range(n):
    cls = heapq.heappop(heap_list)
    if cls[0] >= min(end):
        end.remove(min(end))
        end.append(cls[1])
    else:
        end.append(cls[1])


print(len(end))
