def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(1,(len(score)//m)+1):
        box = score[m*i-m:(m*i)]
        apple_min = min(box)
        answer += apple_min * m
    return answer


k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
print(solution(k,m,score))

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k,m,score))



