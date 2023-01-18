def solution(s):
    answer = ''
    alphas = list(s)
    alpha_list = []
    for token in s:
        if alphas.count(token) == 1:
            alpha_list.append(token)

    alpha_list.sort()
    answer = ''.join(alpha_list)
    return answer


print(solution("abcabcadc"))
