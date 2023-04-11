# computer_count = int(input())
# n = int(input())
#
# roots = [list(map(int, input().split())) for _ in range(n)]
#
# graph = [[0 for _ in range(computer_count + 1)] for _ in range(computer_count + 1)]
#
# count = [False] * 7
# for root in roots:
#     graph[root[0]][root[1]] = 1
#
# for i in range(len(graph[1])):
#     if graph[1][i] == 1:
#         count[i] = True
#         for j in range(len(graph[i])):
#             if graph[i][j] == 1:
#                 count[j] = True
#
# print(count.count(True))

n = int(input())
m = int(input())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n + 1)


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)
print(cnt)