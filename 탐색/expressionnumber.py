def solution(n):
    answer = 0

    for i in range(1,n+1):
        num_sum = 0
        for j in range(i,n+1):
            num_sum += j
            if num_sum == n:
                answer += 1
                break
            elif num_sum > n:
                break
    return answer