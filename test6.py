def solution(s):
    answer = 0
    first_word = ''
    last_word = ''
    first = ''
    for i in range(len(s)):
        if first_word == '':
            first_word += s[i]
            first = s[i]
            continue
        if first == s[i]:
            first_word += s[i]
        else:
            last_word += s[i]

        if len(first_word) == len(last_word):
            answer += 1
            first = ''
            first_word = ''
            last_word = ''
    if len(first_word) > 0:
        answer += 1
    return answer

print(solution('banana'))
print(solution('abracadabra'))
print(solution("aaabbaccccabba"))