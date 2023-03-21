from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
counts = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)


def bfs(start):
    queue = deque([])
    queue.append(start)
    visited[start] = True
    while queue:
        idx = queue.popleft()
        graphs[idx].sort()
        for j in graphs[idx]:
            if not visited[j]:
                counts[j] = counts[idx] + 1
                visited[j] = True
                queue.append(j)


bfs(1)
MAX = max(counts)
idxs = []
for k in range(len(counts)):
    if MAX == counts[k]:
        idxs.append(k)

print(min(idxs), MAX, len(idxs))
