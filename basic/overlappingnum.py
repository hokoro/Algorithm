def solution(my_string):
    answer = ''
    strs = []
    for s in list(str(my_string)):
        if s not in strs:
            strs.append(s)

    answer = ''.join(strs)

    return answer