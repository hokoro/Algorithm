import sys

input = sys.stdin.readline

sentence = input().rstrip()
n = int(input())
print(sentence[n-1])