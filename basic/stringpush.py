def solution(A, B):
    answer = -1
    count = 0
    if A == B:
        answer = 0
        return answer
    As = list(A)

    for i in range(len(A)-1):
        As.insert(0,As.pop())
        count+=1
        if ''.join(As) == B:
            answer = count
            break
    return answer
