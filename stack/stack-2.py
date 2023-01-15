def solution(s):
    answer = True
    letters = []
    last_token = ""
    for token in list(s):
        if last_token == "" and token == ")":
            answer = False
            break
        if last_token == "(" and token == ")":
            letters.pop(len(letters) - 1)
            if len(letters) > 0:
                last_token = letters[len(letters)-1]
            else:
                last_token = ""
            continue
        last_token = token
        letters.append(token)

    if len(letters) > 0:
        answer = False

    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution("')()('"))
print(solution("'(()('"))