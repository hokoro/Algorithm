N,M = map(int,input().split())
min_num_list = []

for i in range(N):
    num_list = list(map(int,input().split()))
    min_num_list.append(min(num_list))


print(max(min_num_list))
