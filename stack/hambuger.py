def solution(ingredient):
    answer = 0
    answer_list = [1, 2, 3, 1]
    stack = []

    for ins in ingredient:
        stack.append(ins)
        if len(stack) >= 4:
            if stack[len(stack) - 4:len(stack)] == answer_list:
                answer += 1
                for i in range(4):
                    stack.pop()
    return answer


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
solution(ingredient=ingredient)
ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
solution(ingredient=ingredient)
