import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if 0 <= x < N and 0 <= y < N:
        if compx[x][y] == 1 and compx[x][y] != 0:
            global cnt
            cnt += 1
            compx[x][y] = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                dfs(nx, ny)
            return True
    return False


cnt = 0
N = int(input())
compx=[]

for _ in range(N):
    compx.append(list(map(int, input())))

house_cnt=[]
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            house_cnt.append(cnt)
            cnt=0
print(len(house_cnt))

house_cnt.sort()
for i in house_cnt:
    print(i)