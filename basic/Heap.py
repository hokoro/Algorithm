import heapq

heap = []

# 삽입
heapq.heappush(heap,50)

heapq.heappush(heap,10)

heapq.heappush(heap,20)

print(heap)


#삭제

data = heapq.heappop(heap)

print(data)
print(heap) # 완전 이진 트리기 때문에 배열 위치가 바뀌어야 한다.