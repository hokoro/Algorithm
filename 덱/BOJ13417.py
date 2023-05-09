from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    card = input().split()
    q = deque()
    q.append(card[0])
    st = card[0]

    for i in range(1,len(card)):
        if st >= card[i]:
            q.appendleft(card[i])
            st = card[i]
        else:
            q.append(card[i])

    print(''.join(q))
