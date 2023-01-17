def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        nums = []
        for j in range(i,i+n):
            nums.append(num_list[j])
        answer.append(nums)
    print(answer)
    return answer


solution([1, 2, 3, 4, 5, 6, 7, 8],2)

