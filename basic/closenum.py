def solution(array, n):
    answer = 0
    diff_nums = []
    array.sort()
    for i in range(len(array)):
        diff_nums.append(abs(array[i] - n))

    answer = array[diff_nums.index(min(diff_nums))]
    return answer


solution([3, 10, 28], 20)