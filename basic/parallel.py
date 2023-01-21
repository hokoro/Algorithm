def solution(dots):
    answer = 0
    point = dots[0]
    otherpoints = dots[1:]
    slope1 = 0
    slope2 = 0
    for _ in range(3):
        slope1 = float((otherpoints[0][1] - point[1]) / (otherpoints[0][0] - point[0]))
        slope2 = float((otherpoints[2][1] - otherpoints[1][1]) / (otherpoints[2][0] - otherpoints[1][0]))
        if slope2 == slope1 and point[1] != otherpoints[1][1]:
            answer = 1

        otherpoints.append(otherpoints.pop(0))

    return answer


print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
