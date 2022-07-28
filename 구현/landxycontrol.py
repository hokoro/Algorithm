
n = int(input())

command = list(input().split())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
move_type = ['R','L','U','D']

x = 1
y = 1
for c in command:
    for i in range(4):
        if c == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx>n or ny > n:
        continue
    x,y = nx,ny

print(x,y)