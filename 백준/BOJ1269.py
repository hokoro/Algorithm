import sys
a, b = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))
answer = set(a_list) ^ set(b_list)

print(len(answer))