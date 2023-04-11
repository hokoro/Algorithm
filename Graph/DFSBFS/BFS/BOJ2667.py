import sys
from collections import deque


n = int(input())
apt = []
for i in range(n):
    apt.append(list(map(int,input())))

visit = [[0] * n for i in range(n)]

dx = [-1,0,1,0]
dy = dx[::-1] # dx 를 역순으로 출력하면 조작 키 전부를 할수 있음

def bfs(x,y,house):
    q = deque()
    q.append((x,y))
    apt[x][y] = 0
    cnt = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx < n and 0 <= ny < n:
                if apt[nx][ny] == house and apt[nx][ny] != 0:
                    q.append((nx,ny))
                    cnt += 1
                    apt[nx][ny] = 0

    return cnt + 1


house_cnt = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            house_cnt.append(bfs(i,j,apt[i][j]))


print(len(house_cnt))

house_cnt.sort()
for i in house_cnt:
    print(i)

print(house_cnt)
print(apt)




# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def dfs(x, y):
#     if 0 <= x < N and 0 <= y < N:
#         if compx[x][y] == 1 and compx[x][y] != 0:
#             global cnt
#             cnt += 1
#             compx[x][y] = 0
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 dfs(nx, ny)
#             return True
#     return False
#
#
# cnt = 0
# N = int(input())
# compx=[]
#
# for _ in range(N):
#     compx.append(list(map(int, input())))
#
# house_cnt=[]
# for i in range(N):
#     for j in range(N):
#         if dfs(i, j):
#             house_cnt.append(cnt)
#             cnt=0
# print(len(house_cnt))
#
# house_cnt.sort()
# for i in house_cnt:
#     print(i)