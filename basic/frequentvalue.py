def solution(array):
    answer = 0
    frequmentcount = 0
    frequmentvalue = 0
    if len(array) == 1:
        return array[0]

    for i in list(set(array)):
        if array.count(i) == frequmentcount:
            frequmentvalue = -1

        if array.count(i) > frequmentcount:
            frequmentvalue = i
            frequmentcount = array.count(i)

    answer = frequmentvalue
    return answer