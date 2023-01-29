import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
number_list2 = list(map(int, sys.stdin.readline().split()))

nums_dict = dict()

for num in number_list:
    nums_dict[num] = nums_dict.setdefault(num, 0) + 1  # 키가 존재 하면 key 값 반환 아니면 0을 반환

for num in number_list2:
    print(nums_dict.setdefault(num, 0), end=' ')
