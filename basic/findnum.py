def solution(num, k):
    answer = -1
    nums = list(str(num))
    for i in range(len(nums)):
        if int(nums[i]) == k:
            answer = i+1
            break

    return answer