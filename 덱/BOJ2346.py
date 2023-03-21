from collections import deque

n = int(input())
answer = []
queue = deque([])
ballon = []
nums = list(map(int,input().split()))
queue.append(nums)

i = 0
while len(queue) != 0:
    move = queue.popleft()
    answer.append(nums.index(move))
    ballon.append(move)
    next = 0
    while True:
        if nums[i+move] not in ballon:
            next = nums[i+move]
        elif nums[i+move] in ballon and move < 0:
            move -= 1
            continue
        else:
            move += 1
            continue
    while True:
        if queue[0] == next:
            break
        queue.append(queue.popleft())

print(answer)