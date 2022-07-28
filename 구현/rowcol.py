row,col = map(int,input().split())

all_data = []

for i in range(row):
    row_data = []
    for j in range(col):
        row_data.append(col * i + (j+1))

    all_data.append(row_data)


print(all_data)
