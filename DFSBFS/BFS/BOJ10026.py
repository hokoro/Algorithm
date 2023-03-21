from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)

input = sys.stdin.readline

n = int(input())
sentences = [input().rstrip() for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
R = 0
G = 0
B = 0
dx = [-1, 0, 1, 0]
dy = dx[::-1]


def bfs(x, y, judgement):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and sentences[nx][ny] == judgement and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


def bfs2(x, y):
    queue = deque()
    queue.append((x, y))
    visited2[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and (sentences[nx][ny] == 'R' or sentences[nx][ny] == 'G') and visited2[nx][
                ny] == 0:
                queue.append((nx, ny))
                visited2[nx][ny] = 1


for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if visited[i][j] == 0 and sentences[i][j] == 'R':
            R += 1
            bfs(i, j, 'R')
        if visited[i][j] == 0 and sentences[i][j] == 'G':
            G += 1
            bfs(i, j, 'G')
        if visited[i][j] == 0 and sentences[i][j] == 'B':
            B += 1
            bfs(i, j, 'B')
sum_ = R + G + B

RandG = 0
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if visited2[i][j] == 0 and (sentences[i][j] == 'R' or sentences[i][j] == 'G'):
            RandG += 1
            bfs2(i, j)

sum_2 = RandG + B

print(sum_, sum_2)
