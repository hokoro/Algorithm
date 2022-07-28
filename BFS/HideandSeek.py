import sys
from collections import deque
input = sys.stdin.readline()

def bfs():
    q = deque()
    q.append(n) # 초기값 5를 추가
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1,x+1,x*2):
            print(j)
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x] +1
                q.append(j)
                print(q)

MAX = 100000
n,k = map(int,input.split())
dist = [0] * (MAX+1)

bfs()
