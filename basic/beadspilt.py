def solution(balls, share):
    value1 = 1
    value2 = 1
    value3 = 1
    for i in range(2,balls+1):
        value1 = value1 * i
    for i in range(2,(balls-share)+1):
        value2 = value2 * i
    for i in range(2,share+1):
        value3 = value3 * i
    return value1 / (value2 * value3)