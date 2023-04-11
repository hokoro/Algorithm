'''
1.출발 노드를 설정합니다
2.최단 거리 테이블을 초기화 (자기자신은 0 / 나머지는 무한대)
3.방문하지 않은 노드중 최단 거리가 가장 짧은 노드를 선택합니다.
4.해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블을 갱신합니다.
5.3/4번 과정을 반복한다.
'''

import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)


for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])