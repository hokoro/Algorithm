import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0

for i in range(1, n - 1):
    for j in range(i, n):
        for k in range(j, n + 1):
            a = {i, j, k}


print(answer)
