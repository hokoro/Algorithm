def solution(nums):
    answer = 0
    pocketmon_list = list()

    for num in nums:
        if len(pocketmon_list) == len(nums)//2:
            break
        if num not in pocketmon_list:
            pocketmon_list.append(num)

    answer = len(pocketmon_list)
    return answer


nums = [3,1,2,3]
print(solution(nums))


nums = [3,3,3,2,2,4]
print(solution(nums))


nums = [3,3,3,2,2,2]
print(solution(nums))
