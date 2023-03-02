import sys
input = sys.stdin.readline


sentence = input().rstrip().split(' ')

word = ''
for token in sentence:
    if token[0].isupper():
        word += token[0]

if word == 'UCPC':
    print(f'I love UCPC')
else:
    print(f'I hate UCPC')