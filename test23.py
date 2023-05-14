def solution(s, skip, index):
    answer = ''
    lower_list = [chr(i) for i in range(97, 97 + 26)]
    for sk in skip:
        lower_list.remove(sk)

    for token in s:
        i = lower_list.index(token)
        i += index
        if i > len(lower_list) -1:
            i %= (len(lower_list))
        answer += lower_list[i]
    return answer


print(solution("aukks", "wbqd", 5))
