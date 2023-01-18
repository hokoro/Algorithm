def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            answer.append(i)
            n /= i
        else:
            i += 1
    answer = list(set(answer))
    answer.sort()
    return answer


print(solution(12))
print(solution(17))
print(solution(420))
