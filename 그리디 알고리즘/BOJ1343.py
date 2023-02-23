lines = input().split('.')

b = True
answer = ''
for line in lines:
    if line == '':
        answer += '.'
        continue

    if len(line) % 2 != 0:
        b = False
        break

    if (len(line) // 2) % 2 != 0:
        token = 'AA' * (len(line) // 2 - 1)
        token = token + 'BB'
        answer += token


    else:
        token = 'AA' * (len(line) // 2)
        answer += token

    answer += '.'
if not b:
    print(-1)

else:
    print(answer[:-1])
