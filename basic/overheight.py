def solution(array, height):
    answer = 0
    for arr in array:
        if height < arr:
            answer += 1
    return answer