t = int(input())

answers = []


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


for _ in range(t):
    nums_len = int(input())
    nums = list(map(int, input().split()))
    graph = [[] * (nums_len + 1) for _ in range(nums_len + 1)]
    visited = [False] * (nums_len + 1)
    for i in range(nums_len):
        graph[i + 1].append(nums[i])
        graph[nums[i]].append(i + 1)
        graph[i].sort()
        # graph[nums[i]].sort()
    count = 0

    for i in range(1, nums_len + 1):
        if not visited[i]:
            count += 1
            dfs(graph, i, visited)

    answers.append(count)

for answer in answers:
    print(answer, end='\n')
