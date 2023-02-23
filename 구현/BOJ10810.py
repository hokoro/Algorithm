import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pockets = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for m in range(i - 1, j):
        pockets[m] = k

for poc in pockets:
    print(poc, end=' ')
