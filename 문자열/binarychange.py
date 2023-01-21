def solution(s):
    answer = []
    count = 0
    remove_zero_count = 0

    while True:
        s_list = list(s)
        if len(s) == 1:
            break

        else:
            zero_count = s_list.count('0')
            remove_zero_count += zero_count
            s = s.replace('0','')
            s = bin(len(s))
            s = s.replace("0b","")
            count += 1
    answer = [count , remove_zero_count]
    return answer





print(solution("01110"))
