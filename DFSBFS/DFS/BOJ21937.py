import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())

graphs = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graphs[b].append(a)

x = int(input())

count = 0


def dfs(c, k, target):
    visited[c] = True
    graphs[c].sort()

    for v in graphs[c]:
        if visited[v] == 0:
            k = k + 1
            visited[v] = k
            dfs(v, k, target)


dfs(x, count, x)

print(visited.count(True) - 1)