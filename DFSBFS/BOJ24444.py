import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,v = map(int,input().split())
count = 1
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph,start,visited):
    global count
    queue = deque([start])
    visited[start] = count

    while queue:
        v = queue.popleft()
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = count


bfs(graph,v,visited)

for i in range(1,n+1):
    print(visited[i])