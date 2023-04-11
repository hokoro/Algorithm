import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])


def dijkstra(start):
    q = []

    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


dijkstra(x)
ans = []

for i in range(1,n+1):
    if distance[i] == k:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for num in ans:
        print(num)
