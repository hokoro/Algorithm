import sys

sentence = sys.stdin.readline()
answer = 0
for token in sentence:
    if token in ['a','e','i','o','u']:
        answer += 1


print(answer)