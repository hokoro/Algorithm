def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    key_list = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for num in numbers:
        print(f'눌러야할 키 패드 {num}')

        if num == 1 or num == 4 or num == 7:
            answer += 'L'
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
        #else:


    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(numbers,hand))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

print(solution(numbers,hand))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'

print(solution(numbers,hand))