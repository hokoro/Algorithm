import sys

input = sys.stdin.readline

n = int(input())

for i in range(1,n+1):
    sentence = '*' * i + ' ' * (n-i)
    print(sentence + sentence[::-1])

for i in range(n-1,0,-1):
    sentence = '*' * i + ' ' * (n-i)
    print(sentence + sentence[::-1])
