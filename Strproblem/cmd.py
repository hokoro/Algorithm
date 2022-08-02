t = int(input())

texts = [input() for _ in range(t)]
common_text = list(texts[0])

for text in texts[1:]:
    for i in range(len(text)):
        if common_text[i] == text[i]:
            common_text[i] = text[i]
        else:
            common_text[i] = '?'

print(''.join(common_text))
