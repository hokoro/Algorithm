def solution(k, score):
    answer = []
    golden_award = []

    for s in score:
        if len(golden_award) < k:
            golden_award.append(s)
        else:
            if s > min(golden_award):
                golden_award.remove(min(golden_award))
                golden_award.append(s)
        answer.append(min(golden_award))
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k, score))
