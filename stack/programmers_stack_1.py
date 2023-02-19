def solution(arr):
    answer = [arr[0]]

    for token in arr[1:]:
        if answer[-1] != token:
            answer.append(token)


    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))

arr = [4,4,4,3,3]
print(solution(arr))
