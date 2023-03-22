import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graphs = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
counts = [0] * (n + 1)


def dfs(s, cnt):
    visited[s] = True
    counts[s] = cnt
    graphs[s].sort()
    for k in graphs[s]:
        if not visited[k]:
            dfs(k, cnt + 1)


for i in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

dfs(r, 0)

for i in range(1, len(counts)):
    if not visited[i]:
        print(-1)
    else:
        print(counts[i])
