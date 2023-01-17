def solution(n):
    answer = 0
    for i in range(4, n + 1):
        count = 1
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 3:
            answer += 1
    return answer


solution(10)