def solution(s):
    nums = []
    for token in s.split(' '):
        print(token)
        if token == 'Z' and len(nums) >0:
            nums.pop()
        else:
            nums.append(int(token))

    return sum(nums)


print(solution('1 2 Z 3'))