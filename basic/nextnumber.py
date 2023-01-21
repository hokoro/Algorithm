def solution(common):
    answer = 0
    gongboolean = True
    value = 0
    if common[1] - common[0] == common[2] - common[1]:
        value = common[1] - common[0]

    elif common[1] // common[0] == common[2] // common[1]:
        gongboolean = False
        value = common[1] // common[0]

    if gongboolean == True:
        answer = common[-1] + value

    else:
        answer = common[-1] * value

    return answer


print(solution([1, 2, 3, 4]))
print(solution([2,4,8]))