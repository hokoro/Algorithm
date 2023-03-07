import sys

input = sys.stdin.readline

n = int(input())

set_ = set()

for _ in range(n):
    command = input().rstrip().split(' ')
    if command[0] == 'add':
        s = {int(command[1])}
        if not set_ >= s:
            set_.add(int(command[1]))
    elif command[0] == 'remove':
        s = {int(command[1])}
        if set_ >= s:
            set_.remove(int(command[1]))
    elif command[0] == 'all':
        set_ = set(range(1, 21))
    elif command[0] == 'empty':
        set_ = set()
    elif command[0] == 'check':
        s = {int(command[1])}
        if set_ >= s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        s = {int(command[1])}
        if set_ >= s:
            set_.remove(int(command[1]))
        else:
            set_.add(int(command[1]))
