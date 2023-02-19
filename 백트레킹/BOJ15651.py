import sys
from itertools import product

input = sys.stdin.readline
n,m = map(int,input().split())
nums = [i for i in range(1, n+1)]


pers = list(product(nums,repeat = m))

for per in pers:
    for j in range(len(per)):
        print(per[j] , end = ' ')
    print()