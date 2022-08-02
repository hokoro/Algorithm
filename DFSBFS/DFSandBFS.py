from collections import deque


def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, v, visited):
    queue = deque([v])

    visited[v] = True

    while queue:
        v = queue.popleft()

        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph_dict = {}
keys = list(graph_dict.keys())

for _ in range(m):
    graph = list(map(int,input().split()))
    keys.append(graph[0])
    keys.append(graph[1])
    keys = list(set(keys))


visited = [False] * (n + 1)

# DFS(graph=graph, v=v, visited=visited)
# print()
# BFS(graph=graph, v=v, visited=visited)
