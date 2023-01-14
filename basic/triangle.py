def solution(sides):
    sides.sort()
    answer = 0
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2

    return answer