import sys

sys.setrecursionlimit(10 ** 6)
MAX = 25 + 10

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y,x):
    global visited, home_count
    visited[y][x] = True
    home_count += 1
    for i in range(4):
        newx = x + dirC[i]
        newy = y + dirR[i]
        if graph[newy][newx] and not visited[newy][newx]:
            dfs(newy,newx)


t = int(sys.stdin.readline())

graph = [[False] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

answers = []
home_count = 0
for i in range(1, t + 1):
    s = input()
    for j in range(1, len(s) + 1):
        if s[j-1] == '1':
            graph[i][j] = True

    for i in range(1, t + 1):
        for j in range(1, t + 1):
            if graph[i][j] and not visited[i][j]:
                home_count = 0
                dfs(i, j)
                answers.append(home_count)
print(len(answers))
answers.sort()
for answer in answers:
    print(answer , end='\n')