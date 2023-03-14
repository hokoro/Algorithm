import sys

input = sys.stdin.readline

last = 1
now = 1

n = int(input())
for _ in range(2, n + 1):
    now, last = last, last + now

print(now)