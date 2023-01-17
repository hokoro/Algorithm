def solution(box, n):
    answer = 1
    for l in box:
        answer *= (l//n)
    return answer