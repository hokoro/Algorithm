def solution(dots):
    answer = 0
    dots.sort(key=lambda x:[x[0],x[1]])

    return (dots[3][0] - dots[0][0]) * (dots[3][1] - dots[0][1])


dots = [[1, 1], [2, 1], [2, 2], [1, 2]]

dots.sort(key=lambda x:[x[0],x[1]])