strs = input()


str_list = set()
for i in range(len(strs)):
    for j in range(0,len(strs)-i):
            str_list.add(strs[j:j+i+1])
print(len(str_list))





