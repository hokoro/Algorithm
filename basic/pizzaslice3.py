def solution(slice, n):
    answer = 0
    answer = n // slice
    n = n % slice

    if n > 0:
        answer += 1


    return answer