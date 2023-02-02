ss = input()
answer = ''

for s in ss:
    if s.isupper():
        answer += s.lower()

    else:
        answer += s.upper()


print(answer)