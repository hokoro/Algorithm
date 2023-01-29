def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    for per in people:
        print(per)

    return answer



print(solution([70, 50, 80, 50],100))
print(solution([70, 80, 50],100))