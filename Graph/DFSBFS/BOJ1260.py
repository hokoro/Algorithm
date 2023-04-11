from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
DFS = []
BFS = []
graph = [[] * (n + 1) for _ in range(n + 1)]
DFS_visited = [False] * (n + 1)
BFS_visited = [False] * (n + 1)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n + 1):
    graph[i].sort()

dfs(graph, v, DFS_visited)
print()
bfs(graph, v, BFS_visited)
