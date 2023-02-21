def solution(array, commands):
    answer = []
    for com in commands:
        nums = array[com[0]-1:com[1]]
        nums.sort()
        answer.append(nums[com[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, command))
