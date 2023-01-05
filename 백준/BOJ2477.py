k = int(input())
information = []
row = []
col = []
lownum = []
for _ in range(6):
    spot, length = map(int, input().split())
    information.append([spot, length])
    if spot == 1 or spot == 2:
        row.append(length)
    else:
        col.append(length)


for i in range(6):
    if information[i][0] == information[(i+2)%6][0]:
        lownum.append(information[(i+1)%6][1])


print(((max(row) * max(col)) - (lownum[0]) * (lownum[1])) * k)
