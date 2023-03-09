import sys

input = sys.stdin.readline

n, m = map(int, input().split())

j = int(input())

spots = [int(input()) for _ in range(j)]

x = 1
answer = 0
for spot in spots:
    start = x
    end = x + m -1
    if start <= spot <= end:
        continue
    if spot < start:
        answer += start - spot
        x = spot
        continue
    if end < spot:
        answer += spot - end
        x = x + spot - end
        continue
print(answer)
