data_list = [1,5,4,2,6,7,11,9,15]

print(data_list)

for i in range(len(data_list)-1):
    for j in range(len(data_list)-1-i):
        if data_list[j] > data_list[j+1]:
            data_list[j], data_list[j+1] = data_list[j+1] , data_list[j]


print(data_list)