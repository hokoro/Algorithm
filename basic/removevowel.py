def solution(my_string):
    answer = ''
    for s in list(my_string):
        if s not in ['a','e','i','o','u']:
            answer += s

    return answer