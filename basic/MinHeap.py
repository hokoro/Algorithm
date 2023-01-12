import heapq

heap = []

heapq.heappush(heap,3)
heapq.heappush(heap,1)
heapq.heappush(heap,2)
heapq.heappush(heap,5)
heapq.heappush(heap,4)

# heap pop 을 수행 시
for i in range(5):
    print(heapq.heappop(heap))



