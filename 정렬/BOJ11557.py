import sys

input = sys.stdin.readline
t = int(input())
answers = []
for _ in range(t):
    count = int(input())
    max_name = ''
    max_L = 0
    for _ in range(count):
        sentence = input().split()
        name, L = sentence[0], int(sentence[1])
        if max_L < L:
            max_name = name
            max_L = L

    answers.append(max_name)

for answer in answers:
    print(answer)
