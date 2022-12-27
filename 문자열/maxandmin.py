def solution(s):
    answer = ''
    num_list = list(map(int , s.split(" ")))

    answer = f"{min(num_list)} {max(num_list)}"
    return answer


s = "1 2 3 4"
print(solution(s))

s = "-1 -2 -3 -4"
print(solution(s))

s = "-1 -1"
print(solution(s))
