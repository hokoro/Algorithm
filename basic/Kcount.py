def solution(i, j, k):
    answer = 0
    for ind in range(i,j+1):
        nums = list(str(ind))
        if str(k) in nums:
            answer += (nums.count(str(k)))
    return answer


solution(1,13,1)