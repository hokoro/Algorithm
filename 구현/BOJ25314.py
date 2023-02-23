import sys

input = sys.stdin.readline

num = int(input())

answer = 'long ' * (num // 4) + 'int'

print(answer)