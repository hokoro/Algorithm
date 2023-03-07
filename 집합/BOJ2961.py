import sys

input = sys.stdin.readline

n = int(input())

foods = []

si = 1
ssn = 0

for _ in range(n):
    i, sn = map(int, input().split())
    foods.append([i, sn])
    si *= i
    ssn += sn

MIN = abs(si - ssn)

if len(foods) > 1:
    for food in foods:
        if abs(si // food[0] - (ssn - food[1])) < MIN:
            si //= food[0]
            ssn -= food[1]
            MIN = abs(si - ssn)

print(MIN)
