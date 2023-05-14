def solution(babbling):
    answer = 0
    can_word = ['aya', 'ye', 'woo', 'ma']

    for i in range(len(babbling)):
        for j in can_word:
            if j in babbling[i]:
                babbling[i] = babbling[i].replace(j, '', 1)

        if babbling[i] == '':
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution('woayao'))