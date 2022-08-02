t = int(input())

texts = [list(input().split(' ')) for _ in range(t)]

for text in texts:
    for i in range(len(text)):
        text[i] = text[i][::-1]

for text in texts:
    for i in range(len(text)):
        print(text[i], end=' ')
