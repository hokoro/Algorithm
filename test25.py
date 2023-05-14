def solution(ingredient):
    answer = 0
    stacks = []
    for ing in ingredient:
        stacks.append(ing)
        if len(stacks) >= 4:
            if stacks[len(stacks)-4:len(stacks)] == [1,2,3,1]:
                answer += 1
                for _ in range(4):
                    stacks.pop()
    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))