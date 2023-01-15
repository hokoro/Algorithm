def solution(my_string):
    answer = 0
    for s in list(my_string):
        if '1'<= s <= '9':
            answer += int(s)
    return answer