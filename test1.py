def solution(dartResult):
    answer = []
    score = []
    bonus = []
    option = []
    token = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            token += dartResult[i]
        elif dartResult[i] in ['S', 'D', 'T']:
            bonus.append(dartResult[i])
            score.append(token)
            token = ''
            if i + 1 < len(dartResult) and dartResult[i + 1].isdigit():
                option.append('')
        elif dartResult[i] in ['#', '*']:
            option.append(dartResult[i])
    if len(option) < 3:
        option.append('')
    for s, b, o in zip(score, bonus, option):
        num = int(s)
        if b == 'S':
            num = num ** 1
        if b == 'D':
            num = num ** 2
        if b == 'T':
            num = num ** 3
        if o == '#':
            num = num * -1
        if o == '*':
            if len(answer) > 0:
                answer[-1] = answer[-1] * 2
            num = num * 2
        answer.append(num)
    return sum(answer)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))