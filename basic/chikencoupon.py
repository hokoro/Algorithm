def solution(chicken):
    answer = 0
    coupon = chicken

    while True:
        if coupon < 10:
            break
        answer += (coupon // 10)
        coupon = coupon // 10 + coupon % 10
    return answer

print(solution(1081))


