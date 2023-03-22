import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

graphs = [[] for _ in range(n + 1)]
visited = [[-1, 0] for _ in range(n + 1)]
count = 1
for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)


def dfs(r):
    global count
    graphs[r].sort()
    for g in graphs[r]:
        if visited[g][0] == -1:
            count += 1
            visited[g] = [visited[r][0] + 1, count]
            dfs(g)


visited[r][0] = 0
dfs(r)

ans = 0
for v in visited[1:]:
    ans += (v[0] * v[1])

print(ans)
# print(ts)
# print(ds)
