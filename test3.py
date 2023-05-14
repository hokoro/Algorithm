from collections import Counter
def solution(X, Y):
    stacks = []
    Y_list = Counter(list(Y))
    print(Y_list)
    for i in range(len(X)):
        if Y_list[X[i]] > 0:
            stacks.append(X[i])
            Y_list[X[i]] -= 1

    print(stacks)
    if len(stacks) == 0:
        answer = '-1'
    else:
        answer = str(int(''.join(stacks)))
    return answer


print(solution("100","2354"))
print(solution("100" , "00235"))