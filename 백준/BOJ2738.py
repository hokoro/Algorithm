a, b = map(int, input().split())

a_list = [list(map(int, input().split())) for _ in range(a)]
b_list = [list(map(int, input().split())) for _ in range(a)]

for i in range(a):
    for j in range(b):
        a_list[i][j] += b_list[i][j]


for i in range(a):
    for j in range(b):
        print(a_list[i][j] , end = ' ')
    print('')
