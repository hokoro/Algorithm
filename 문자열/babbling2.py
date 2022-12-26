def solution(babbling):
    answer = 0
    babbling_list = ["aya", "ye", "woo", "ma"]
    bab_list = []
    for babb in babbling:
        bab_list = []
        if babb in babbling_list:
            answer += 1
            continue
        else:
            bab_str = ''
            for bab in babb:
                bab_str += bab
                if bab_str in babbling_list and bab_str not in bab_list:
                    bab_list.append(bab_str)
                    bab_str = ''

            if "".join(bab_list) == babb:
                answer += 1

    return answer


babbing = ["aya", "yeaya", "u", "maa"]
print(solution(babbing))

babbing = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbing))
