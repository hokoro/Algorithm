def dfs(graph , v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)


# dfs 반복을 이용한 구현

# def DFS_stack(graph, root):
#     visited = []
#     stack = [root]  # 시작 위치
#
#     while stack:
#         print('stack', stack)
#         n = stack.pop()  # 스택의 앞에서부터
#         print('n = ',n)
#         if n not in visited:
#             visited.append(n)
#             stack += graph[n] - set(visited)
#
#         print('stack_re',stack)
#         print('visited',visited)
#
#     return visited
#
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}
# root_node = 1
# print(DFS_stack(graph_list,root_node))
