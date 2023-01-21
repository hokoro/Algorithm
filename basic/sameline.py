def solution(lines):
    answer = 0
    line_list = [0 for _ in range(200)]
    for i in range(len(lines)):
        for j in range(lines[i][0] + 100 , lines[i][1] +100):
            line_list[j] += 1

    for i in range(200):
        if line_list[i] > 1:
            answer += 1

    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))