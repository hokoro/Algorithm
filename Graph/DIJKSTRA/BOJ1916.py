import heapq
import sys

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())


def dijkstra(s,e):
    q = []

    heapq.heappush(q, [0, s])
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])
        if now == e:
            break

dijkstra(start,end)

print(distance[end])
