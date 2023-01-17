def solution(age):
    answer = ''
    for token in list(str(age)):
        answer += (chr(97+int(token)))
    return answer


