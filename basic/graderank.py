def solution(score):
    answer = []
    means = [(sc[0] + sc[1])/2 for sc in score]
    means.sort(reverse=True)
    for sc in score:
        answer.append(means.index((sc[0] + sc[1]) / 2) + 1)
    return answer


print(solution([[80, 70], [90, 50], [40, 70], [50, 80]]))