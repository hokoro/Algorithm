import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
answer = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        visited[r][c] = True
        answer += 1
    x, y = r, c
    flag = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                flag = False

    if flag:
        if d == 0:
            if 0 <= r + 1 < n and 0 <= c < m:
                r += 1
        elif d == 1:
            if 0 <= r < n and 0 <= c - 1 < m:
                c -= 1
        elif d == 2:
            if 0 <= r - 1 < n and 0 <= c < m:
                r -= 1
        else:
            if 0 <= r < n and 0 <= c + 1 < m:
                c += 1
        if board[r][c] == 1:
            break
        else:
            continue
    else:
        if d == 0:
            d = 3
            if 0 <= r < n and 0 <= c - 1 < m:
                if board[r][c - 1] == 0:
                    c -= 1
        elif d == 1:
            d = 0
            if 0 <= r - 1 < n and 0 <= c < m:
                if board[r - 1][c] == 0:
                    r -= 1
        elif d == 2:
            d = 1
            if 0 <= r < n and 0 <= c + 1 < m:
                if board[r][c + 1] == 0:
                    c += 1
        else:
            d = 2
            if 0 <= r + 1 < n and 0 <= c + 1 < m:
                if board[r + 1][c] == 0:
                    r += 1

print(answer)
