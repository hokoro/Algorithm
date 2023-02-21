def solution(sizes):
    #가로세로 상관말기
    width = []
    height = []
    answer = 0
    for i in range (len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    answer=max(width)*max(height)
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
