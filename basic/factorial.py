def solution(n):
    answer = 0
    num = 1
    i = 1
    while num != n:
        i += 1
        num *= i
        if num > n:
            i -= 1
            break

    answer = i
    return answer
