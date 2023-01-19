def solution(sides):
    answer = 0
    for i in range(max(sides) - min(sides)+1 , max(sides) + min(sides)):
        temporay_list = list(sides)
        temporay_list.append(i)
        value = max(temporay_list)
        temporay_list.remove(value)
        if value < temporay_list[0] + temporay_list[1]:
            answer += 1


    return answer