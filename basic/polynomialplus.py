def solution(polynomial):
    x_value = 0
    value = 0
    polynomial = polynomial.split(' + ')

    for token in polynomial:
        if 'x' in token:
            if len(token) == 1:
                x_value += 1
            else:
                x_value += int(token[:-1])
        else:
            value += int(token)

    if x_value > 0 and value > 0:
        if x_value == 1:
            return f'x + {value}'
        return f'{x_value}x + {value}'
    elif x_value == 0 and value >0:
        return f'{value}'
    else:
        if x_value == 1:
            return 'x'
        return f'{x_value}x'



print(solution("3x + 7 + x"))
print(solution("x + x + x"))