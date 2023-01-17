def solution(order):
    answer = 0
    for num in list(str(order)):
        if num in ['3','6','9']:
            answer += 1
    return answer