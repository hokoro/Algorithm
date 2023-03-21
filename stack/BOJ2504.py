import sys

input = sys.stdin.readline

sentence = input().strip()
sentence = sentence.replace('()', 2)
sentence = sentence.replace('[]', 3)

sentence = list(sentence)
caculator = []

for i in range(len(sentence)):
    if sentence[i].isdigit() and (sentence[i-1] ,sentence[i+1]) == ('(',')'):
        caculator.append(sentence[i])
        caculator.append('x')
        caculator.append('2')
        continue
    if sentence[i].isdigit() and (sentence[i-1] ,sentence[i+1]) == ('[',']'):
        caculator.append(sentence[i])
        caculator.append('x')
        caculator.append('3')
        continue
    if caculator[-1].isdigit() and not sentence[i].isdigit():
        caculator.append('+')
        continue

