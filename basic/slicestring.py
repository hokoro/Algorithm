def solution(my_str, n):
    answer = []
    strs = list(my_str)
    for i in range(0,len(strs),n):
        answer.append(''.join(strs[i:i+n]))

    return answer