# def solution(x, y):
#     answer = ''
#     number_list = []
#     x = list(x)
#     y = list(y)
#     for i in range(len(x)):
#         if x[i] in y:
#             number_list.append(int(x[i]))
#             y.remove(x[i])
#
#     if not number_list:
#         answer = '-1'
#     elif max(number_list) < 1:
#         answer = '0'
#     else:
#         number_list.sort(reverse=True)
#         answer = ''.join(str(n) for n in number_list)
#
#     return answer

from collections import Counter


def solution(X, Y):
    answer = '-1'

    list_X, list_Y = list(X), list(Y)
    set_X, set_Y = set(list_X), set(list_Y)
    cnt_X, cnt_Y = Counter(list_X), Counter(list_Y)

    intersection = set_X & set_Y

    if intersection:
        answer = ''
        sorted_number = sorted(intersection, reverse=True)

        for num in sorted_number:
            answer += num * min(cnt_X[num], cnt_Y[num])

        if sum(list(map(int, list(answer)))) == 0:
            answer = "0"

    return answer


x = "100"
y = "2345"

print(solution(x, y))

x = "100"
y = "203045"

print(solution(x, y))

x = "100"
y = "123450"

print(solution(x, y))

x = "12321"
y = "42531"

print(solution(x, y))

x = "5525"
y = "1255"

print(solution(x, y))
