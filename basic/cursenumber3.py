def solution(n):
    answer = 1
    numbers = []
    num = 1
    while len(numbers) != n:
        if num % 3 == 0 or '3' in str(num):
            num += 1
            continue
        numbers.append(num)
        num += 1
    return numbers[-1]


print(solution(15))
print(solution(40))
