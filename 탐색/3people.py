def solution(number):
    answer = 0

    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for z in range(j + 1, len(number)):
                if number[i] + number[j] + number[z] == 0:
                    answer += 1
    return answer


number = [-2, 3, 0, 2, -5]

print(solution(number))

number = [-3, -2, -1, 0, 1, 2, 3]

print(solution(number))

number = [-1, 1, -1, 1]

print(solution(number))
