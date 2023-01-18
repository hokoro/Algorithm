def solution(array):
    answer = 0
    for num in array:
        nums = list(str(num))
        answer += nums.count('7')
    return answer