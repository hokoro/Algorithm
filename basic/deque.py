from collections import deque

de = deque()

for i in range(3,0 ,-1):
    de.appendleft(i)
    de.append(i)

for _ in range(6):
    #print(de.pop()) 오른쪽 부터 원소 제거 후 리턴
    print(de.popleft()) # 왼쪽 부터 원소 제거 후 리턴