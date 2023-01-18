def solution(my_string):
    answer = 0
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s , ' ')

    numbers = my_string.split(' ')
    for num in numbers:
        if num == '':
            continue
        else:
            answer += (int(num))
    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))