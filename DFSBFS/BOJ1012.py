import sys

sys.setrecursionlimit(10 ** 6)

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]
t = int(sys.stdin.readline())
MAX = 50 + 10

def dfs(y, x):
    global visited
    visited[y][x] = True  # 이미 방문을 했다
    for i in range(4):
        newy = y + dirR[i]
        newx = x + dirC[i]
        if graph[newy][newx] and not visited[newy][newx]:
            dfs(newy, newx)


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y + 1][x + 1] = True  # 벌레들이 서식하는 위치

    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1

    print(answer)
