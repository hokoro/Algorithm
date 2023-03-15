import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

cnt = 0


def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)


for i in range(1, len(visited)):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
