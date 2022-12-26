def solution(survey, choices):
    answer = ''
    nature_dict = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    for s, c in zip(survey, choices):
        s_list = list(s)
        if c == 1:
            nature_dict[s_list[0]] += 3
        elif c == 2:
            nature_dict[s_list[0]] += 2
        elif c == 3:
            nature_dict[s_list[0]] += 1
        elif c == 4:
            continue
        elif c == 5:
            nature_dict[s_list[1]] += 1
        elif c == 6:
            nature_dict[s_list[1]] += 2
        else:
            nature_dict[s_list[1]] += 3

    key_list = list(nature_dict.keys())
    value_list = list(nature_dict.values())

    for i in range(0,8,2):
        if value_list[i] == value_list[i+1]:
            answer += key_list[i]
        else:
            if value_list[i] > value_list[i+1]:
                answer += key_list[i]
            else:
                answer += key_list[i+1]

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]

choices = [5, 3, 2, 7, 5]

solution(survey, choices)

survey = ["TR", "RT", "TR"]

choices = [7, 1, 3]

solution(survey, choices)


