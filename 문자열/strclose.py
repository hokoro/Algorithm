def solution(s):
    answer = []
    s_list = []
    count = 0
    for st in s:
        if st not in s_list:
            answer.append(-1)
            s_list.append(st)
        else:
            for i in range(len(s_list)-1, -1, -1):
                if s_list[i] == st:
                    answer.append(count - i)
                    s_list.append(st)
                    break
        count += 1
    return answer


s = "banana"
print(solution(s))

s = "foobar"
print(solution(s))
