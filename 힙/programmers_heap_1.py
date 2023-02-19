import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) >= 2:
        min_ = heapq.heappop(scoville)
        if min_ >= K:
            break
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_ + min2 * 2)
            answer += 1
    if scoville[0] < K:
        return -1
    return answer


scoville = [1, 2, 9, 3, 12, 10]
K = 7
print(solution(scoville, K))
