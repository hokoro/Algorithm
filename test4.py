from collections import Counter


def solution(participant, completion):
    answer = ''
    Comp = Counter(completion)
    for p in participant:
        if Comp[p] > 0:
            Comp[p] -= 1
        else:
            answer = p
    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
