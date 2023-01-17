def solution(n):
    answer = 0
    pizzabox = 6
    while pizzabox % n != 0:
        pizzabox += 6

    answer = pizzabox // 6

    return answer