def solution(array):
    answer = []
    answer_value = 0
    answer_index = 0

    for i in range(len(array)):
        if answer_value < array[i]:
            answer_value = array[i]
            answer_index = i

    answer.append(answer_value)
    answer.append(answer_index)
    return answer