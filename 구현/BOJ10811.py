import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pockets = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    pockets[i-1:j] = reversed(pockets[i-1:j])
for poc in pockets:
    print(poc, end=' ')
