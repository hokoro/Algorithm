def solution(denum1, num1, denum2, num2):
    answer = []
    desum = (denum1 * num2) + (denum2 * num1)
    nsum = num1 * num2

    for i in range(1, nsum + 1):
        if nsum % i == 0 and desum % i == 0:
            desum = desum / i
            nsum = nsum / i
    answer = [int(desum), int(nsum)]
    return answer


denum1 = 1
num1 = 2
denum2 = 3
num2 = 4

print(solution(denum1, num1, denum2, num2))
