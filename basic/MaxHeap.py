import heapq

heap = []

values = [5,1,3,2,4]

# 부호를 - 로 하여 최소 힙을 만든 다음 출력 할때는 부호를 바꾸어서 출력한다.
for value in values:
    heapq.heappush(heap,-value)

print(heap)

for i in range(5):
    print(-heapq.heappop(heap))