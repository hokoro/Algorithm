def solution(topping):
    answer = 0
    for i in range(len(topping)):
        if len(set(topping[:i+1])) == len(set(topping[i+1:])):
            answer += 1
    return answer


topping = [1,2,1,3,1,4,1,2]

print(solution(topping))
