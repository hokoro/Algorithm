def solution(emergency):
    answer = [0 for _ in range(len(emergency))]
    sorteds = sorted(emergency,reverse=True)
    for i in range(0,len(sorteds)):
        answer[emergency.index(sorteds[i])] = i+1

    return answer