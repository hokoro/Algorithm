def solution(t, p):
    answer = 0
    p_len = len(p)
    p_num = int(p)

    for i in range(0, len(t)):
        if len(t[i:i + p_len]) == p_len and p_num >= int(t[i:i + p_len]):
            answer += 1

    return answer


t = "3141592"
p = "271"

print(solution(t, p))

t = "500220839878"
p = "7"

print(solution(t, p))

t = "10203"
p = "15"

print(solution(t, p))
