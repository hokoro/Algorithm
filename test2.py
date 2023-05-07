def solution(cards1, cards2, goal):
    answer = ''
    stacks = []
    for g in goal:
        if cards1[0] == g:
            stacks.append(g)
            cards1.remove(g)
        elif cards2[0] == g:
            stacks.append(g)
            cards2.remove(g)
        else:
            return 'No'

    if stacks == goal:
        answer = 'Yes'
    return answer


print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
