# def solution(k, tangerine):
#     answer = 0
#     tan_count = [0] * (max(tangerine) + 1)
#
#     for tan in tangerine:
#         tan_count[tan] += 1
#
#     while k != 0:
#         if k < max(tan_count):
#             answer = 1
#             break
#         k -= max(tan_count)
#         answer += 1
#         tan_count.remove(max(tan_count))
#     return answer

from collections import Counter


def solution(k, tangerine):
    answer = 0
    sum = 0
    tan = Counter(tangerine).most_common()

    for t in tan:
        sum += t[1]
        answer += 1
        if sum >= k:
            return answer

    return answer

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
print(solution(k, tangerine))
