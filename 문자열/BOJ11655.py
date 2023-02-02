my_strs = input()
answer = ''

for s in my_strs:
    if s.isalpha():
        if s.isupper():
            if ord(s) + 13 > 90:
                answer += chr((ord(s) + 13) % 90 + 64)
                continue

            answer += chr(ord(s) + 13)
        else:
            if ord(s) + 13 > 122:
                answer += chr((ord(s) + 13) % 122 + 96)
                continue
            else:
                answer += chr(ord(s) + 13)
    else:
        answer += s

print(answer)
