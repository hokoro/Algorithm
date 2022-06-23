num = int(input())

num_list = set(range(2, num + 1))

for i in range(2, num + 1):
    if i in num_list:
        num_list -= set(range(2 * i, num + 1, i))

print(len(num_list))
