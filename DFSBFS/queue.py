# 5-2-3-7-DEL-1-4-DEL

from collections import deque

queue = deque()

num_input = [5,2,3,7,'del',1.4,'del']

for num in num_input:

    if num == 'del':
        print(queue.popleft())

    else:
        queue.append(num)


#print(queue[::-1]) queue 에서는 slice 가 먹지 않는다
print(queue)
queue.reverse()
print(queue)