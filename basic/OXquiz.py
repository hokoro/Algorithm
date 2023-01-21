def solution(quiz):
    answer = []

    for q in quiz:
        q = q.split('=')
        expression = q[0]
        value = q[1]
        if eval(expression) == int(value):
            answer.append('O')
        else:
            answer.append('X')
    return answer