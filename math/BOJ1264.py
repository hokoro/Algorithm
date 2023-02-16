while True:
    sentence = input()
    answer = 0
    if sentence == '#':
        break

    for token in sentence:
        token = token.lower()
        if token in ['a', 'e', 'i', 'o', 'u']:
            answer += 1
            continue

    print(answer)
