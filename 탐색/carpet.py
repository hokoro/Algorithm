def solution(brown, yellow):
    answer = []
    # brown + yellow = x * y
    # yellow = x-2 * y-2 (x>0 , y>0 )
    # brown = (x*y) - yellow
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer