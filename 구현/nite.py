yx = input()

y = int(ord(yx[0]) - 96)
x = int(yx[1])

dx = [-1,1,2,2,1,-1,-2,-2]
dy = [-2,-2,-1,1,2,2,1,-1]

# print(x,y)

count =0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        count+=1



print(count)