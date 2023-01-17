def solution(my_string):
    answer = ''
    strs = list(my_string)

    for i in range(len(strs)):
        strs[i] = strs[i].lower()

    strs.sort()

    answer = "".join(strs)

    return answer