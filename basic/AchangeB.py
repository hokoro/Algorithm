def solution(before, after):
    answer = 0
    count = 0
    afters = list(after)
    for b in before:
        if b in afters:
            count += 1
            afters.remove(b)

    if count == len(after):
        answer = 1
    return answer