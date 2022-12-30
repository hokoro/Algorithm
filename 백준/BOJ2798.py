import sys
import itertools
n,m = map(int,sys.stdin.readline().split())

num_list = list(map(int,input().split()))

three = list(itertools.combinations(num_list,3))
answer = 0
for num in three:
    if num[0] + num[1] + num[2] == m:
        answer = num[0] + num[1] + num[2]
        break
    elif answer < num[0] + num[1] + num[2] < m:
        answer = num[0] + num[1] + num[2]


print(answer)