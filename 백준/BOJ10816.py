import sys
n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
number_list2 = list(map(int, sys.stdin.readline().split()))

for n in number_list2:
    print(number_list.count(n), end=' ')
