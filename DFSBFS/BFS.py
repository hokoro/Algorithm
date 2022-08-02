from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])  # 순서를 담은 스택

    visited[start] = True  # 첫번째 방문은 True

    while queue:
        v = queue.popleft()  # queue 에 스택을 담고

        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
