import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

r, c, K = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(r)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = dx[::-1]
answer = 0


def dfs(x, y, cnt):
    global answer
    if cnt == K:
        if (x, y) == (0, c - 1):
            answer += 1

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graphs[nx][ny] != 'T':
                graphs[nx][ny] = 'T'
                dfs(nx, ny, cnt + 1)
                graphs[nx][ny] = '.'  # 탐색이 끝나면 다시 원래 모습으로


graphs[r - 1][0] = 'T'
dfs(r - 1, 0, 1)
print(answer)
