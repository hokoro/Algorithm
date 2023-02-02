words = input()

bomb_word = input()

word_list = []
answer = ''

for token in words:
    word_list.append(token)
    if len(word_list) < len(bomb_word):
        continue

    else:
        if ''.join(word_list[-len(bomb_word):]) == bomb_word:
            for _ in range(len(bomb_word)):
                word_list.pop()

if len(word_list) == 0:
    answer = 'FRULA'

else:
    answer = ''.join(word_list)

print(answer)
