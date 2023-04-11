import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graphs = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
counts = [0] * (n + 1)


def dfs(s, last):
    visited[s] = True
    counts[s] = last
    for k in graphs[s]:
        if not visited[k]:
            dfs(k, s)


for _ in range(n - 1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
dfs(1, 0)

for i in range(2,len(counts)):
    print(counts[i])