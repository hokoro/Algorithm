# import sys
#
# test_case = int(sys.stdin.readline())
#
# num_list = list(map(int, sys.stdin.readline().split()))
#
# num_list2 = sorted(num_list)
# index_count = 0
# last_num = num_list2[0]
# for num in num_list2:
#     if last_num == num:
#         num_list[num_list.index(num)] = index_count
#     else:
#         index_count += 1
#         num_list[num_list.index(num)] = index_count
#     last_num = num
#
# for num in num_list:
#     print(num, end=' ')

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')
