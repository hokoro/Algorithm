my_str = input().strip()
alpha = dict()
my_str_set = list(set(my_str))
for c in my_str_set:
    print(my_str.count(c))
    alpha[c] = my_str.count(c)

keys_list = list(alpha.keys())
count_list = list(alpha.values())



print(keys_list)
print(count_list)

print(count_list.index(max(count_list)))