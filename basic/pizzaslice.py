def solution(n):
    answer = 0
    answer += (n // 7)
    n = n % 7

    if n > 0:
        answer += 1


    return answer