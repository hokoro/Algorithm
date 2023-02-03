from collections import deque
import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    answer = 0
    n,m = map(int,sys.stdin.readline().split())
    prints = deque(list(map(int,sys.stdin.readline().split())))
    indexs = deque([i for i in range(len(prints))])
    print(prints)
    print(indexs)
    
