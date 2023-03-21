import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
bans = [[] * (m+1) for _ in range(m+1)]

for _ in range(m):
    a,b = map(int,input().split())
    bans[a].append(b)
    bans[b].append(a)
for i in range(1, n - 1):
    for j in range(i, n):
        for k in range(j, n + 1):
            a = {i, j, k}


print(answer)
