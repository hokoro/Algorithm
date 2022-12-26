def solution(s):
    answer = 0
    save_point1 = 0
    save_point2 = 0

    for i in s:
        if save_point1 == save_point2:
            answer += 1
            a = i
        if i == a:
            save_point1 += 1
        else:
            save_point2 += 1
    return answer


s = "banana"
print(solution(s))
