def solution(spell, dic):
    answer = 2
    for d in dic:
        temporary_spell = list(spell)
        d_list = list(d)
        for token in d_list:
            if token in temporary_spell:
                temporary_spell.remove(token)
        if len(temporary_spell) == 0:
            answer = 1
            break
    return answer


print(solution(["z", "d", "x"] , 	["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))