import sys

input = sys.stdin.readline

n , l = map(int,input().split())
hnums = list(map(int,input().split()))
hnums.sort()

for num in hnums:
    if l >= num:
        l += 1

print(l)