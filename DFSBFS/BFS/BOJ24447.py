import sys
from collections import deque

input = sys.stdin.readline

n,m,s = map(int,input().split())

graphs = [[] for _ in range(n+1)]
visited = [[-1,0] for _ in range(n+1)]
count = 0
count += 1

def bfs(l):
    global count
    queue = deque([])
    queue.append(l)
    visited[l] = [0,count]
    while queue:
        l = queue.popleft()
        graphs[l].sort()
        for k in graphs[l]:
            if visited[k][0] == -1:
                count += 1
                visited[k] = [visited[l][0] + 1 , count]
                queue.append(k)


for _ in range(m):
    a,b = map(int,input().split())
    graphs[a].append(b)
    graphs[b].append(a)

bfs(s)
result = 0
for v in visited:
    result += (v[0] * v[1])
print(result)