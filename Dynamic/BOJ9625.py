import sys

input = sys.stdin.readline

n = int(input())
lastA, lastB = 1, 0
nowA, nowB = 0, 1
for i in range(2, n + 1):
    tempA, tempB = nowA, nowB
    nowA, nowB = nowA + lastA, nowB + lastB
    lastA,lastB = tempA , tempB


print(f'{nowA} {nowB}')
