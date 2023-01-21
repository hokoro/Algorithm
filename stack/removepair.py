def solution(s):
    answer = 0
    tokens = []

    for i in s:
        if len(tokens) == 0:
            tokens.append(i)
            continue

        if tokens[-1] == i:
            tokens.pop()

        else:
            tokens.append(i)

    if len(tokens) == 0:
        answer = 1

    return answer



