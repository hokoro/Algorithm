def solution(numbers, k):
    answer = 0
    count = 0
    i = 0
    while count != k-1:
        count += 1
        i = (i+2)%len(numbers)

    answer = numbers[i]
    return answer