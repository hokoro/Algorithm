words = input()
tokens = []
token = ''
answer = ''
bracket_bool = False

for w in words:
    if w == '<':
        bracket_bool = True
        answer = answer + token[::-1]
        token = '<'
        continue
    elif w == '>':
        bracket_bool = False
        token = token + '>'
        answer = answer + token
        token = ''
    elif w == ' ' and bracket_bool == False:
        answer = answer + token[::-1] + ' '
        token = ''
        continue
    else:
        token = token + w

if len(token) > 0:
    answer = answer + token[::-1]


print(answer)
