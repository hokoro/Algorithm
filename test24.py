def solution(keymap, targets):
    answer = []
    keys_len = len(keymap)
    for target in targets:
        count = 0
        for token in target:
            stacks = []
            for i in range(keys_len):
                if keymap[i].find(token,0,len(keymap[i])) >= 0:
                    stacks.append(keymap[i].find(token,0,len(keymap[i])))
            if len(stacks) == 0:
                answer.append(-1)
                break
            count += (min(stacks) + 1)
        if count > 0:
            answer.append(count)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
