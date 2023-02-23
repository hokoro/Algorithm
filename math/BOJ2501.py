import sys

input = sys.stdin.readline
n,k = map(int,input().split())

tokens = []

for i in range(1, int(n ** (1 / 2)) + 1):
    if n % i == 0:
        tokens.append(i)
        if (i ** 2) != n:
            tokens.append(n // i)

tokens.sort()

if len(tokens) < k:
    print(0)
else:
    print(tokens[k-1])