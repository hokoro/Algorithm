import sys
from collections import deque

A, B, N, M = map(int, input().split())
visited = [False] * 100001
cnt = [0] * 100001
q = deque()


def bfs(N):
    q.append(N)
    while q:
        x = q.popleft()
        for i in (x + A, x + B, x * A, x * B, x - A, x - B, x + 1, x - 1):
            if i == M:
                print(cnt[x] + 1)
                sys.exit(0)
            if 0 <= i < 100001 and not visited[i]:
                cnt[i] = cnt[x] + 1
                visited[i] = True
                q.append(i)


bfs(N)
print(cnt[M])
