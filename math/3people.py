from itertools import combinations
def solution(number):
    answer = 0
    nums_c = list(combinations(number , 3))

    for nums in nums_c:
        if nums[0] + nums[1] + nums[2] == 0:
            answer += 1
    return answer


number = [-2, 3, 0, 2, -5]
