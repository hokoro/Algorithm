a, b = map(str, input().split())

answer = ''
a_tokens = a[::-1]
b_tokens = b[::-1]

a = ''
b = ''
for at in a_tokens:
    if a == '' and at == '0':
        continue
    a += at

for bt in b_tokens:
    if b == '' and bt == '0':
        continue
    b += bt

tokens = str(eval(f'{a} + {b}'))[::-1]

for token in tokens:
    if answer == '' and token == '0':
        continue
    answer += token

print(int(answer))
