def solution(number, limit, power):
    iron_Weights = 0
    for knight in range(1, number + 1):
        weapon_Pow = 0
        for num in range(1, int(knight ** 0.5) + 1):
            if knight % num == 0:
                weapon_Pow += 1
                if num ** 2 != knight: #제곱이 되는 약수라면 중복되는걸 방지한다.
                    weapon_Pow += 1
            if weapon_Pow > limit:
                weapon_Pow = power
                break
        iron_Weights += weapon_Pow
    return iron_Weights


number = 5
limit = 3
power = 2

print(solution(number, limit, power))

number = 10
limit = 3
power = 2

print(solution(number, limit, power))
