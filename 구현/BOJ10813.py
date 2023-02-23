import sys

n, m = map(int, input().split())

pockets = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    pockets[i - 1] , pockets[j-1] = pockets[j-1] , pockets[i-1]

for poc in pockets:
    print(poc, end=' ')
